# Generated by Django 4.0.2 on 2022-02-13 23:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0019_alter_weeklybox_date_issued'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklybox',
            name='date_issued',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 14, 12, 3, 40, 306988)),
        ),
    ]
