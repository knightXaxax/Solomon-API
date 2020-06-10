# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Checked(models.Model):
    item_id = models.IntegerField()
    line = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checked'


class Checking(models.Model):
    item_id = models.IntegerField()
    line = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checking'


class ForChecking(models.Model):
    item_id = models.IntegerField()
    line = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'for_checking'


class ForEncoding(models.Model):
    item_id = models.IntegerField()
    line = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'for_encoding'


class ForInvoicing(models.Model):
    item_id = models.IntegerField()
    line = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'for_invoicing'


class ForPacking(models.Model):
    item_id = models.IntegerField()
    line = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'for_packing'


class ForPicking(models.Model):
    item_id = models.IntegerField()
    line = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'for_picking'


class Invoiced(models.Model):
    item_id = models.IntegerField()
    line = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoiced'


class Invoicing(models.Model):
    item_id = models.IntegerField()
    line = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoicing'


class OrderProcessingQueue(models.Model):
    customer_id = models.CharField(max_length=100)
    so_number = models.IntegerField()
    order_qty = models.IntegerField()
    order_total_price = models.IntegerField()
    order_date = models.DateField()
    status_id = models.IntegerField()
    remarks_id = models.IntegerField()
    warehouse_id = models.IntegerField()
    unserved_id = models.IntegerField()
    for_picking_id = models.IntegerField()
    picking_id = models.IntegerField()
    picked_id = models.IntegerField()
    for_checking_id = models.IntegerField()
    checking_id = models.IntegerField()
    checked_id = models.IntegerField()
    for_packing_id = models.IntegerField()
    packing_id = models.IntegerField()
    packed_id = models.IntegerField()
    for_encoding_id = models.IntegerField()
    for_invoicing_id = models.IntegerField()
    invoicing_id = models.IntegerField()
    invoiced_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_processing_queue'


class Packed(models.Model):
    item_id = models.IntegerField()
    line = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'packed'


class Packing(models.Model):
    item_id = models.IntegerField()
    line = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'packing'


class Picked(models.Model):
    item_id = models.IntegerField()
    line = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picked'


class Picking(models.Model):
    item_id = models.IntegerField()
    line = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picking'


class RemarksInfo(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'remarks_info'


class StatusInfo(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'status_info'


class TransmittalInfo(models.Model):
    so_number = models.IntegerField(primary_key=True)
    order_date = models.DateField()
    customer_id = models.CharField(max_length=100)
    purchase_order_date = models.DateField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'transmittal_info'


class Unserved(models.Model):
    item_id = models.IntegerField()
    line = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unserved'


class WarehouseInfo(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'warehouse_info'
