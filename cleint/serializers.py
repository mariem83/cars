from .models import Car,Client,Company
from rest_framework import serializers
class CarSer(serializers.ModelSerializer):
    class Meta :
        model = Car
        fields = '__all__'
class ClientSer(serializers.ModelSerializer):
    class Meta :
        model = Client
        fields = '__all__'

class CompanySer(serializers.ModelSerializer):
    class Meta :
        model = Company
        fields = '__all__'
