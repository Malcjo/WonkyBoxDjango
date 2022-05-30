# Generated by Django 4.0.1 on 2022-01-28 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmstead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Vegetables', 'Vegetables'), ('Fruits', 'Fruits'), ('Others', 'Others')], max_length=200, null=True)),
                ('farms', models.ManyToManyField(to='Api.Farmstead')),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('produce', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Api.produce')),
            ],
        ),
    ]
