# Generated by Django 4.0.1 on 2022-01-28 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weeklybox',
            name='produce',
        ),
        migrations.AddField(
            model_name='weeklybox',
            name='produce',
            field=models.ManyToManyField(to='Api.Produce'),
        ),
    ]