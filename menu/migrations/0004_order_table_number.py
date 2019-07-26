# Generated by Django 2.2.2 on 2019-07-26 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_order_is_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='table_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]