from django.db import transaction, IntegrityError, connections # database libraries and packages
from .models import OrderProcessingQueue # Order Processing Queue Table class from ORM App Model


class Database:

    # constructor method
    def __init__(self, dbname):
        self._name = "Database"
        self.__dbname = dbname

    # method for raw querying
    def _rawQuery(self, query, execValues):
        try:
            with transaction.atomic():
                return OrderProcessingQueue.objects.using(self.__dbname).raw(query, execValues)
        except IntegrityError:
            return "query error"

    # method for direct raw querying
    def _rawQueryDirect(self, query, execValues):
        with connections[self.__dbname].cursor() as cursor:
            cursor.execute(query, execValues)
            return cursor