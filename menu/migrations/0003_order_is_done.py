# Generated by Django 2.2.2 on 2019-06-19 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20190619_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]