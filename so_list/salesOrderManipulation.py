from .models import OrderProcessingQueue, Unserved, ForPicking, Picking, Picked, ForChecking, Checking, Checked, ForPacking, Packing, Packed, ForEncoding, ForInvoicing, Invoicing, Invoiced
from .database import Database # Custom Database class
from django.db import transaction, IntegrityError
from .algorithms import TravellingSalesManAlgorithm # Travelling Salesman Algorithm class
import threading, datetime, dateutil.relativedelta


class SalesOrderManipulation:
    
    
    def __init__(self): 
        self._name = "SalesOrderManipulation"
        self.__ordersDb = Database("orders")
        self._scannedSoNumberFinalData = {}
        self.__models = {
            'unserved' : Unserved,
            'for_picking' : ForPicking,
            'picking' : Picking,
            'picked' : Picked, 
            'for_checking' : ForChecking,
            'checking' : Checking,
            'checked' : Checked,
            'for_packing' : ForPacking,
            'packing' : Packing,
            'packed' : Packed,
            'for_encoding' : ForEncoding,
            'for_invoicing' : ForInvoicing,
            'invoicing' : Invoicing,
            'invoiced' : Invoiced
        }
        self._changeStatusResponse = ""
        self._analyzedSalesOrderData = ""
        self._cycleCounts = []
        self._salesOrdersForToday = []
        self._pendingSalesOrders = []
        self.__statusNames = [str.replace(str(status.name).lower(), " ", "_") for status in self.__ordersDb._rawQuery("SELECT `id`, `name` FROM `status_info`;", [])]


    def scannedSoNumberData(self, soNumber):
        allData = []
        ordersData = []
        finalOrdersData = []

        for order in self.__ordersDb._rawQuery("SELECT  oq.`id`, oq.`so_number`, oq.`status_id`, si.`name` as status_name, oq.`remarks_id`, ri.`name` as remarks_name FROM `order_processing_queue` oq INNER JOIN `status_info` si ON oq.`status_id` = si.`id` INNER JOIN `remarks_info` ri ON oq.`remarks_id` = ri.`id` WHERE oq.`so_number` =  %s;", [soNumber]):
            ordersData.append(
                {
                    'order_queue_id' : order.id,
                    'soNumber' : order.so_number,
                    'status_id' : order.status_id,
                    'status' : str.replace(str(order.status_name).lower(), " ", "_"),
                    'remarks_id' : order.remarks_id,
                    'remarks' : str.replace(str(order.remarks_name).lower(), " ", "_")
                }
            ) 

        for orderData in ordersData:
            
            for order in self.__ordersDb._rawQuery("SELECT oq.status_id, oq.`id`, oq.`customer_id`, oq.`order_qty`, oq.`order_total_price`, oq.`order_date`, u.`id` as unserved_id, u.`item_id`, u.`line`, u.`qty`, u.`total_price`, date(u.`created_at`) as unserved_date, bi.`bin_id`, ii.`isbn`, ii.`description`, ii.`unit_price`, pt.`name` as product_type FROM `order_processing_queue` oq INNER JOIN `"+orderData['status']+"` u ON oq.`"+orderData['status']+"_id` = u.`id` INNER JOIN `items`.`bin_lists` bi ON u.`item_id` = bi.`item_id` INNER JOIN `items`.`items_info` ii ON u.`item_id` = ii.`part` INNER JOIN `items`.`product_type` pt ON ii.`product_type_id` = pt.`id` WHERE oq.`id` = %s;", [orderData['order_queue_id']]):
                finalOrdersData.append({
                    'orderQueueId' : orderData['order_queue_id'],
                    'soNumber' : orderData['soNumber'],
                    'customerId' : order.customer_id,
                    'status' : orderData['status'],
                    'statusId' : order.status_id,
                    'remarks' : orderData['remarks'],
                    'remarksId' : orderData['remarks_id'],
                    str(orderData['status'])+"Id" : order.unserved_id,
                    'itemId' : order.item_id,
                    'line' : order.line,
                    'isbn' : order.isbn,
                    'description' : order.description,
                    'productType' : order.product_type,
                    'unitPrice' : order.unit_price,
                    'qty' : order.qty,
                    'totalPrice' : order.total_price,
                    'unservedDate' : order.unserved_date,
                    'orderQty' : order.order_qty,
                    'orderTotalPrice' : order.order_total_price,
                    'orderDate' : order.order_date,
                    'binNumber' : order.bin_id
                })

        for status in self.__ordersDb._rawQuery("SELECT `id`, `name` FROM `status_info`;", []):
            statusName = str.replace(str(status.name).lower(), " ", "_")
            tempData = []
            
            for data in finalOrdersData:
                tempData.append(data) if data['status'] == statusName else ""
            
            allData.append({
                statusName : tempData
            })

        if len([data[item] for data in allData for item in data if item == 'unserved'][0]) != 0:
            fastestRoute = TravellingSalesManAlgorithm([data[item] for data in allData for item in data if item == 'unserved'][0])

            for data in allData:
                for item in data:
                    if item == 'unserved':
                        data[item] = fastestRoute.generateRoute()

        salesOrdersToChange = [
            {
                'salesOrder' : [data[item] for data in allData for item in data if item == 'unserved'][0],
                'forStatusId': 2,
                'forRemarksId': 2,
                'origin' : 'unserved',
                'destination' : 'for_picking',
            },
            {
                'salesOrder' : [data[item] for data in allData for item in data if item == 'picked'][0],
                'forStatusId': 5,
                'forRemarksId': 2,
                'origin' : 'picked',
                'destination' : 'for_checking',
            },
            {
                'salesOrder' : [data[item] for data in allData for item in data if item == 'checked'][0],
                'forStatusId': 8,
                'forRemarksId': 2,
                'origin' : 'checked',
                'destination' : 'for_packing',
            }
        ]

        changeStatusProcess = [threading.Thread(target=self.changeSoStatusPhase, args=(dataParams,) ) for dataParams in salesOrdersToChange]
        
        for process in changeStatusProcess:
            process.daemon = True
            process.start()
        
        for process in changeStatusProcess:
            process.join()

        self._scannedSoNumberFinalData = {
            'salesOrders' : allData,
        }


    def changeSoStatusPhase(self, params):
        if len(params['salesOrder']) != 0:
            for orderData in params['salesOrder']:
                try:
                    with transaction.atomic():
                        destinationStatus = self.__models[params['destination']](item_id=orderData['itemId'], line=orderData['line'], qty=orderData['qty'], total_price=orderData['totalPrice'], created_at=datetime.datetime.now())        
                        destinationStatus.save(using='orders')

                        originStatus = self.__models[orderData['status']].objects.using('orders').get(id=orderData[str(orderData['status'])+"Id"])
                        originStatus.delete()

                        orderProcessingQueue = OrderProcessingQueue.objects.using('orders').get(id=orderData['orderQueueId'])
                        orderProcessingQueue.status_id = params['forStatusId']
                        orderProcessingQueue.remarks_id = orderData['remarksId']
                        orderProcessingQueue.save(using='orders')

                        self.__ordersDb._rawQueryDirect("UPDATE order_processing_queue SET "+params['origin']+"_id = %s, "+params['destination']+"_id = %s WHERE id = %s", [
                            0,
                            destinationStatus.id,
                            orderData['orderQueueId']
                        ])

                        self._changeStatusResponse = "success"
                except IntegrityError:
                    self._changeStatusResponse = "failed"
                    break
        else:
            self._changeStatusResponse = "empty"


    def getCycleCounts(self):
            for status in self.__statusNames:
                tempData = []
                for order in self.__ordersDb._rawQuery("SELECT substring(order_date, 1, 4) as order_year, count("+status+"_id) as id FROM `order_processing_queue` WHERE "+status+"_id > 0 GROUP BY order_year ORDER BY order_year DESC", []):
                    tempData.append({
                        'year' : order.order_year,
                        'count' : order.id
                    })     
                self._cycleCounts.append({
                    'status' : str.replace(str.replace(str(status), " ", ""), "_", " ").title(),
                    'data' : tempData
                }) 

            self._cycleCounts.append({
                'status' : 'For Processing',
                'data' : self._cycleCounts[0]['data']
            })


    def getSalesOrdersForToday(self):
        threads = [ threading.Thread(target=self.__getSalesOrdersByStatus, args=(status, ) ) for status in self.__statusNames ]
        for T in threads:
            T.daemon = True
            T.start()

        for T in threads:
            T.join()


    def __getSalesOrdersByStatus(self, status):
        salesOrders = [{
            'orderQueueId' : order.order_queue_id,
            'soNumber' : order.so_number,
            'customerId' : order.customer_id,
            'customerName' : order.customer_name,
            'statusId' : order.status_id,
            'status' : order.status_name,
            'remarksId' : order.remarks_id,
            'remarks' : order.remarks_name,
            'statusQueueId' : order.status_queue_id,
            'itemId' : order.item_id,
            'line' : order.line,
            'isbn' : order.isbn,
            'description' : order.description,
            'productType' : order.product_type,
            'unitPrice' : order.unit_price,
            'qty' : order.qty,
            'totalPrice' : order.total_price,
            'date' : str(order.date),
            'orderQty' : order.order_qty,
            'orderTotalPrice' : order.order_total_price,
            'orderDate' : str(order.order_date),
            'binNumber' : order.bin_id,
        }
        for order in self.__ordersDb._rawQuery("SELECT oq.`id` as order_queue_id, oq.`so_number`, oq.`customer_id`, si.`id` as status_id, si.`name` as status_name, ri.`id` as remarks_id, ri.`name` as remarks_name, s.`id` as status_queue_id, s.`item_id`, s.`line`, ii.`isbn`, ii.`description`, pt.`name` as product_type, ii.`unit_price`, s.`qty`, s.`total_price`, date(s.`created_at`) as date, oq.`order_qty`, oq.`order_total_price`, oq.`order_date`, bi.`bin_id`, pt.`id`, ci.`id`, ci.`name` as customer_name FROM `order_processing_queue` oq INNER JOIN `"+status+"` s ON oq.`"+status+"_id` = s.`id` INNER JOIN `status_info` si ON oq.`status_id` = si.`id` INNER JOIN `customers`.`customer_info` ci ON oq.`customer_id` = ci.`id` INNER JOIN `remarks_info` ri ON oq.`remarks_id` = ri.`id` INNER JOIN `items`.`items_info` ii ON s.`item_id` = ii.`part` INNER JOIN `items`.`product_type` pt ON ii.`product_type_id` = pt.`id` INNER JOIN `items`.`bin_lists` bi ON s.`item_id` = bi.`item_id` WHERE date(oq.`order_date`) IN (CURRENT_DATE);", []) ]
        self._salesOrdersForToday.append({
            'status' : str.replace(str.replace(str(status), " ", ""), "_", " ").title(),
            'data' : salesOrders
        })


    def getPendingSalesOrders(self):
        dateFormat = '%Y-%m-%d'
        pendingSalesOrderDates = [ datetime.datetime.strftime(order.order_date, dateFormat)  for order in self.__ordersDb._rawQuery("SELECT oq.`id`, oq.`order_date` FROM `order_processing_queue` oq INNER JOIN `unserved` u ON oq.`unserved_id` = u.`id` WHERE so_number NOT IN (SELECT so_number FROM `transmittal_info` GROUP BY so_number) GROUP BY oq.`order_date` ORDER BY oq.`order_date` ASC;", [])] 
        threads = [threading.Thread(target=self.identifyPendingSalesOrders, args=(orderDate, ) ) for orderDate in pendingSalesOrderDates ]
        for T in threads:
            T.daemon = True
            T.start()
        
        for T in threads:
            T.join()


    def identifyPendingSalesOrders(self, orderDate):
        salesOrders = [{
            'orderQueueId' : order.order_queue_id,
            'soNumber' : order.so_number,
            'customerId' : order.customer_id,
            'statusId' : order.status_id,
            'status' : order.status_name,
            'remarksId' : order.remarks_id,
            'remarks' : order.remarks_name,
            'statusQueueId' : order.status_queue_id,
            'itemId' : order.item_id,
            'line' : order.line,
            'isbn' : order.isbn,
            'description' : order.description,
            'productType' : order.product_type,
            'unitPrice' : order.unit_price,
            'qty' : order.qty,
            'totalPrice' : order.total_price,
            'date' : order.date,
            'orderQty' : order.order_qty,
            'orderTotalPrice' : order.order_total_price,
            'orderDate' : order.order_date,
            'binNumber' : order.bin_id,
        } for order in self.__ordersDb._rawQuery("SELECT oq.`id` as order_queue_id, oq.`so_number`, oq.`customer_id`, si.`id` as status_id, si.`name` as status_name, ri.`id` as remarks_id, ri.`name` as remarks_name, s.`id` as status_queue_id, s.`item_id`, s.`line`, ii.`isbn`, ii.`description`, pt.`name` as product_type, ii.`unit_price`, s.`qty`, s.`total_price`, date(s.`created_at`) as date, oq.`order_qty`, oq.`order_total_price`, oq.`order_date`, bi.`bin_id`, pt.`id` FROM `order_processing_queue` oq INNER JOIN `unserved` s ON oq.`unserved_id` = s.`id` INNER JOIN `status_info` si ON oq.`status_id` = si.`id` INNER JOIN `remarks_info` ri ON oq.`remarks_id` = ri.`id` INNER JOIN `items`.`items_info` ii ON s.`item_id` = ii.`part` INNER JOIN `items`.`product_type` pt ON ii.`product_type_id` = pt.`id` INNER JOIN `items`.`bin_lists` bi ON s.`item_id` = bi.`item_id` WHERE date(oq.`order_date`) IN(%s) and oq.`so_number` NOT IN (SELECT `so_number` FROM `transmittal_info` GROUP BY `so_number`);", [ str(orderDate) ]) ]
        
        if len(salesOrders) != 0:
            self._pendingSalesOrders.append({
                orderDate : salesOrders
            })
    