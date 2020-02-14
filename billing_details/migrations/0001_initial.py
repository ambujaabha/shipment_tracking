# Generated by Django 2.0.3 on 2020-02-12 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0002_auto_20200212_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutationCode', models.CharField(blank=True, max_length=120)),
                ('firstName', models.CharField(blank=True, max_length=120)),
                ('surname', models.CharField(blank=True, max_length=120)),
                ('email', models.EmailField(blank=True, max_length=120)),
                ('company', models.CharField(blank=True, max_length=120)),
                ('vatNumber', models.IntegerField(blank=True, max_length=120)),
                ('chamberOfCommerceNumber', models.IntegerField(blank=True, max_length=120)),
                ('orderReference', models.CharField(blank=True, max_length=120)),
                ('deliveryPhoneNumber', models.IntegerField(blank=True, max_length=120)),
                ('address', models.ForeignKey(on_delete=True, to='address.Address')),
            ],
        ),
    ]
