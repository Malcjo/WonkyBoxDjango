from rest_framework import serializers
from .models import Farmstead, Produce, WeeklyBox

class ProduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produce
        fields = ['id', 'name', 'category', 'image', 'description', 'seasonal_information', 'storage', 'additional_information', ]

class FarmsteadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmstead
        fields = ['id', 'name', 'email', 'region', 'image', 'location', 'produces', 'description', 'farmers_story']

class WeeklyBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyBox
        fields = ['id', 'region', 'date_issued', 'day', 'produce']