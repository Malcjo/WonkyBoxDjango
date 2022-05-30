from django.db import models
from datetime import datetime


class Produce(models.Model):
    CATEGORY =(
        ('Vegetables', 'Vegetables'),
        ('Fruits', 'Fruits'),
        ('Others', 'Others'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=200, null=True, choices = CATEGORY)
    image = models.ImageField(blank = True, null = True, upload_to='produce_images/')
    description = models.TextField(null=True, blank=True)
    seasonal_information = models.TextField(null=True, blank=True)
    storage = models.TextField(null=True, blank=True)
    additional_information = models.TextField(null=True, blank=True)
    
    def __str__(self):
		    return self.name

class Farmstead(models.Model):
    REGION =(
        ('Auckland', 'Auckland'),
        ('Northland', 'Northland'),
        ('Bay of Plenty', 'Bay of Plenty'),
        ('Waikato', 'Waikato'),
        ('Taranaki', 'Taranaki'),
        ('Hawkes Bay', 'Hawkes Bay'),
        ('Gisborne', 'Gisborne'),
        ('Manawatu-Wanganui', 'Manawatu-Wanganui'),
        ('Wellington', 'Wellington')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=200, null=True, choices = REGION)
    image = models.ImageField(blank = True, null = True, upload_to='farmstead_images/')
    location = models.CharField(max_length=200, null=True, blank=True)
    produces = models.ManyToManyField(Produce)
    description = models.TextField(null=True, blank=True)
    farmers_story = models.TextField(null=True, blank=True)

    def __str__(self):
		    return self.name

class WeeklyBox(models.Model):
    class Meta:
        verbose_name_plural = 'Weekly Boxes'

    REGION =(
        ('Auckland', 'Auckland'),
        ('Northland', 'Northland'),
        ('Bay of Plenty', 'Bay of Plenty'),
        ('Waikato', 'Waikato'),
        ('Taranaki', 'Taranaki'),
        ('Hawkes Bay', 'Hawkes Bay'),
        ('Gisborne', 'Gisborne'),
        ('Manawatu-Wanganui', 'Manawatu-Wanganui'),
        ('Wellington', 'Wellington')
    )
    DAYS =(
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    id = models.AutoField(primary_key=True)
    region = models.CharField(max_length=200, null=True, choices = REGION)
    date_issued = models.DateTimeField(default=datetime.now())
    day = models.CharField(max_length=200, null=True, choices = DAYS)
    produce = models.JSONField(null=True)