from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import EmployeesInfo
from django.db import transaction, IntegrityError
from .database import Database
from .models import OnlineEmployees
import json, datetime


@csrf_exempt
def login(request):
    params = json.loads(request.POST['params'])
    db = Database('employees')
    data = [{
        'employeeId' : employee.id, 
        'passwd' : employee.password,
        'name' : employee.name,
        'user' : employee.username,
        'position' : employee.position,
        'level' : employee.level,
        'email' : employee.email,
    } for employee in db._rawQuery("SELECT a.id, a.`username`, a.`password`, a.name, c.position, d.level, a.email FROM employees_info a INNER JOIN accounts_info b ON a.id = b.employee_id INNER JOIN roles_info c ON b.role_id = c.id INNER JOIN access_levels d ON c.access_id = d.id WHERE username = %s;",[
        params['user']
    ])]
    data = data[0] if len(data) > 0 else ""

    if len(data) == 0:
        data = {'msg': "Incorrect username."}
    else :
        if data['passwd'] != params['passwd']:
            data = {'msg': "Incorrect password."}
        else:
            try:
                with transaction.atomic():
                    onlineEmployees = [onlineEmployee.employee_id for onlineEmployee in db._rawQuery("SELECT * FROM online_employees;", [])]
                    if data['employeeId'] not in onlineEmployees:
                        onlineEmployee = OnlineEmployees(employee_id=data['employeeId'], temp_code=str(data['employeeId']) + str(data['user']), created_at=datetime.datetime.now())
                        data = {
                            'employeeId' : data['employeeId'], 
                            'name': data['name'],
                            'user' : data['user'],
                            'position': data['position'],
                            'level': data['level'],
                            'tempCode' : onlineEmployee.temp_code,
                            'email' : data['email'],
                            'msg' : 'success'
                        }
                        onlineEmployee.save(using='employees')
            except IntegrityError:
                data = {'msg': "Login error."}

    data = { 'data' : data }

    return JsonResponse(data, safe=True)


@csrf_exempt
def logout(request):
    params = json.loads(request.POST['params'])
    try:
        with transaction.atomic():
            onlineEmployees = OnlineEmployees.objects.using('employees').get(temp_code=params['tempCode'])
            onlineEmployees.delete()
            params = {'msg' : 'success'}
    except IntegrityError:
        params = {'msg' : 'failed'}

    return JsonResponse(params, safe=False)