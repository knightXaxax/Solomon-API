from django.db import transaction, IntegrityError, connections # database libraries and packages
from .models import EmployeesInfo


class Database:

    # constructor method
    def __init__(self, dbname):
        self._name = "Database"
        self.__dbname = dbname

    # method for raw querying
    def _rawQuery(self, query, execValues):
        try:
            with transaction.atomic():
                return EmployeesInfo.objects.using(self.__dbname).raw(query, execValues)
        except IntegrityError:
            return "query error"

    # method for direct raw querying
    def _rawQueryDirect(self, query, execValues):
        with connections[self.__dbname].cursor() as cursor:
            cursor.execute(query, execValues)
            return cursor.fetchall()