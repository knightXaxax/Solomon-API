# Generated by Django 3.0.3 on 2020-04-02 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('line', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'checked',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Checking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('line', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'checking',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ForChecking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('line', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'for_checking',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ForEncoding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('line', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'for_encoding',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ForInvoicing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('line', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'for_invoicing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ForPacking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('line', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'for_packing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ForPicking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('line', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'for_picking',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Invoiced',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('line', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'invoiced',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Invoicing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('line', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'invoicing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderProcessingQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=100)),
                ('so_number', models.IntegerField()),
                ('order_qty', models.IntegerField()),
                ('order_total_price', models.IntegerField()),
                ('order_date', models.DateField()),
                ('status_id', models.IntegerField()),
                ('remarks_id', models.IntegerField()),
                ('warehouse_id', models.IntegerField()),
                ('unserved_id', models.IntegerField()),
                ('for_picking_id', models.IntegerField()),
                ('picking_id', models.IntegerField()),
                ('picked_id', models.IntegerField()),
                ('for_checking_id', models.IntegerField()),
                ('checking_id', models.IntegerField()),
                ('checked_id', models.IntegerField()),
                ('for_packing_id', models.IntegerField()),
                ('packing_id', models.IntegerField()),
                ('packed_id', models.IntegerField()),
                ('for_encoding_id', models.IntegerField()),
                ('for_invoicing_id', models.IntegerField()),
                ('invoicing_id', models.IntegerField()),
                ('invoiced_id', models.IntegerField()),
            ],
            options={
                'db_table': 'order_processing_queue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Packed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('line', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'packed',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Packing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('line', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'packing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Picked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('line', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'picked',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Picking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('line', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'picking',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RemarksInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'remarks_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StatusInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'status_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TransmittalInfo',
            fields=[
                ('so_number', models.IntegerField(primary_key=True, serialize=False)),
                ('order_date', models.DateField()),
                ('customer_id', models.CharField(max_length=100)),
                ('purchase_order_date', models.DateField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'transmittal_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Unserved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('line', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'unserved',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WarehouseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'warehouse_info',
                'managed': False,
            },
        ),
    ]
