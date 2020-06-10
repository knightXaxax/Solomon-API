# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccessLevels(models.Model):
    level = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'access_levels'


class AccountsInfo(models.Model):
    employee_id = models.IntegerField()
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accounts_info'


class EmployeesInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=7)
    email = models.TextField()
    contact_num = models.IntegerField()
    username = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=200)
    created_by = models.TextField()
    updated_by = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'employees_info'


class OnlineEmployees(models.Model):
    employee_id = models.IntegerField()
    temp_code = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'online_employees'


class RolesInfo(models.Model):
    position = models.CharField(max_length=30)
    access_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'roles_info'
