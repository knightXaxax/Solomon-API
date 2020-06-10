from django.urls import path
from .views import getScannedSoNumberData, processingSoNumberData, getCycleCount, getSalesOrdersForToday, getPendingSalesOrders


urlpatterns = [
    path('_get_scanned_so_number_data/', getScannedSoNumberData), # route for getting the data from the database using the scanned so number and generate a fastest route
    path('_processing_so_number_data/', processingSoNumberData), # route for processing the picking data from the scanned so number
    path('_get_cycle_count/', getCycleCount),
    path('_get_sales_orders_for_today/', getSalesOrdersForToday),
    path('_get_pending_sales_orders/', getPendingSalesOrders),
]