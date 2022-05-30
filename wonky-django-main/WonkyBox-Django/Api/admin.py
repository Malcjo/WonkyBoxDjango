from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from .models import *

class FarmsteadModel(admin.ModelAdmin):
    list_filter = ('name', 'region', 'location', 'produces')
    list_display = ('name', 'region', 'location')

@admin.register(Produce)
class ProduceModel(admin.ModelAdmin):
    list_filter = ('name', 'category')
    list_display = ('name', 'category')

@admin.register(WeeklyBox)
class WeeklyBoxModel(admin.ModelAdmin):
    list_filter = ('date_issued', 'region', 'day', 'produce')
    list_display = ('date_issued', 'region', 'day')

class FarmsteadAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
admin.site.register(Farmstead, FarmsteadAdmin)