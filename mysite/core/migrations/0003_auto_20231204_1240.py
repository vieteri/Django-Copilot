# Generated by Django 3.2.7 on 2023-12-04 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_purchase_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcollection',
            name='user',
        ),
        migrations.AddField(
            model_name='purchase',
            name='purchaser',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]