# Generated by Django 5.1.6 on 2025-05-06 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_delete_service'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentDelivery',
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
    ]
