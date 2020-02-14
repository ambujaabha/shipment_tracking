# Generated by Django 2.0.3 on 2020-02-12 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transportId', models.CharField(blank=True, max_length=120)),
                ('transporterCode', models.CharField(blank=True, max_length=120)),
                ('trackAndTrace', models.CharField(blank=True, max_length=120)),
                ('shippingLabelId', models.CharField(blank=True, max_length=120)),
                ('shippingLabelCode', models.CharField(blank=True, max_length=120)),
            ],
        ),
    ]
