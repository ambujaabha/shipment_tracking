# Generated by Django 2.0.3 on 2020-02-12 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderItemId', models.CharField(blank=True, max_length=120)),
                ('orderId', models.CharField(blank=True, max_length=120)),
                ('latestDeliveryDate', models.DateTimeField(blank=True, max_length=120)),
                ('orderDate', models.DateTimeField(auto_now_add=True)),
                ('ean', models.IntegerField(blank=True, max_length=120)),
                ('title', models.CharField(blank=True, max_length=120)),
                ('quantity', models.CharField(blank=True, max_length=120)),
                ('offerPrice', models.CharField(blank=True, max_length=120)),
                ('offerCondition', models.CharField(blank=True, max_length=120)),
                ('offerReference', models.CharField(blank=True, max_length=120)),
                ('fulfilmentMethod', models.CharField(blank=True, max_length=120)),
            ],
        ),
    ]