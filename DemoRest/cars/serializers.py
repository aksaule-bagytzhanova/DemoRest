from django.db.models import fields
from re import L
from rest_framework import serializers
from cars.models import  Car

class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'