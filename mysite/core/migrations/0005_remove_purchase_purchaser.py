# Generated by Django 3.2.7 on 2023-12-03 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_purchase_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='purchaser',
        ),
    ]