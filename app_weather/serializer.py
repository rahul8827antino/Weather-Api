from app_weather.models import *
from rest_framework import serializers
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name','desc','temp_min','temp_max','pressure','humidity','sunrise_time','sunset_time']