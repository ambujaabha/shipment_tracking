# Generated by Django 2.0.3 on 2020-02-29 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200226_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderId',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
