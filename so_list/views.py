from django.http import JsonResponse # Json Library for API return types
from django.views.decorators.csrf import csrf_exempt # package library for exempting the method to the csrf auth
from .salesOrderManipulation import SalesOrderManipulation # Sales Order Manipulation class
import urllib.request, json, threading, base64


@csrf_exempt
def getScannedSoNumberData(request):
    # params = {
    #     'soNumber' : 204856
    # }
    params = json.loads(request.POST['params'])
    params['soNumber'] = int(params['soNumber'])

    salesOrderManipulate = SalesOrderManipulation()

    processThread = threading.Thread(target=salesOrderManipulate.scannedSoNumberData, args=(params['soNumber'], ))
    processThread.daemon = True
    processThread.start()
    processThread.join()

    processedData = salesOrderManipulate._scannedSoNumberFinalData

    return JsonResponse(processedData, safe=True)    


@csrf_exempt
def processingSoNumberData(request):
    # getData = urllib.request.urlopen("http://127.0.0.1:8000/_api/_so_list/_get_scanned_so_number_data/")
    # params = {
    #     'salesOrder' : json.loads(getData.read())['salesOrders'][0]['unserved'],
    #     'forStatusId': 2,
    #     'forRemarksId': 2,
    #     'origin' : 'unserved',
    #     'destination' : 'for_picking',
    # } 
    params = json.loads(request.POST['params'])
    params['forStatusId'] = int(params['statusId'])
    params['forRemarksId'] = int(params['forRemarksId'])

    salesOrderManipulate = SalesOrderManipulation()

    processThread = threading.Thread(target=salesOrderManipulate.changeSoStatusPhase, args=(params, ))
    processThread.daemon = True
    processThread.start()
    processThread.join()    

    data = {
        'msg' : salesOrderManipulate._changeStatusResponse
    }

    return JsonResponse(data, safe=True)


@csrf_exempt
def getCycleCount(request):
    salesOrderManipulate = SalesOrderManipulation()

    processThread = threading.Thread(target=salesOrderManipulate.getCycleCounts )
    processThread.daemon = True
    processThread.start()
    processThread.join()
    
    processData = { 'cycleCounts' : salesOrderManipulate._cycleCounts }

    return JsonResponse(processData, safe=True)


@csrf_exempt
def getSalesOrdersForToday(request):
    salesOrderManipulate = SalesOrderManipulation()
    processThread = threading.Thread(target=salesOrderManipulate.getSalesOrdersForToday )
    processThread.daemon = True
    processThread.start()
    processThread.join()
    
    processData = {
        'salesOrdersForToday' : salesOrderManipulate._salesOrdersForToday
    }

    return JsonResponse(processData, safe=True)


@csrf_exempt
def getPendingSalesOrders(request):
    salesOrderManipulate = SalesOrderManipulation()

    processThread = threading.Thread(target=salesOrderManipulate.getPendingSalesOrders )
    processThread.daemon = True
    processThread.start()
    processThread.join()
    
    processData = {
        'pendingSalesOrder' : salesOrderManipulate._pendingSalesOrders
    }

    return JsonResponse(processData, safe=True)