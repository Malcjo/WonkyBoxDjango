# Generated by Django 4.0.2 on 2022-02-10 22:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0009_alter_weeklybox_date_issued'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklybox',
            name='date_issued',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]
