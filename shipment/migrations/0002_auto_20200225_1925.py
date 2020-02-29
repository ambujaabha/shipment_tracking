# Generated by Django 2.0.3 on 2020-02-25 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='shipmentItems',
        ),
        migrations.AddField(
            model_name='shipment',
            name='shipmentItems',
            field=models.ForeignKey(default=1, on_delete=True, to='order.Order'),
            preserve_default=False,
        ),
    ]