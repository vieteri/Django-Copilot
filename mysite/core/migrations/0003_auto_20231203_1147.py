# Generated by Django 3.2.7 on 2023-12-03 11:47

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
            model_name='purchase',
            name='amount',
        ),
        migrations.AddField(
            model_name='purchase',
            name='purchaser',
            field=models.ForeignKey(default='Anonymous', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
