# Generated by Django 4.0.1 on 2022-02-11 00:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0013_image_alter_weeklybox_date_issued'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='produce',
            name='caption',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='produce',
            name='image',
            field=models.ImageField(null=True, upload_to='img/%y'),
        ),
        migrations.AlterField(
            model_name='weeklybox',
            name='date_issued',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 11, 13, 59, 43, 36791)),
        ),
    ]
