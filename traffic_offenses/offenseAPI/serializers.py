from rest_framework import serializers
from management.models import Officer, Vehicle, Person
from .models import Offense
from django.core.exceptions import ObjectDoesNotExist

class OffenseSerializer(serializers.ModelSerializer):
    vehicle = serializers.CharField(required=True)
    timestamp = serializers.CharField()
    comentarios = serializers.CharField(source='comments')

    class Meta:
        model = Offense
        fields = ['vehicle', 'timestamp', 'comentarios']
    
    def create(self, validated_data):
        license_plate = validated_data.pop('vehicle', None)
        try:
            vehicle = Vehicle.objects.get(license_plate=license_plate)
        except ObjectDoesNotExist:
            raise serializers.ValidationError({"placa_patente": "No se encontró un vehículo con esa placa."})
        
        offense = Offense(vehicle=vehicle, **validated_data)
        offense.save()
        return offense

class OffenseSerializerOut(serializers.ModelSerializer):
    timestamp = serializers.CharField()
    comentarios = serializers.CharField(source='comments')

    class Meta:
        model = Offense
        fields = ['timestamp', 'comentarios']
        
class VehicleSerializer(serializers.ModelSerializer):
    infracciones = OffenseSerializerOut(many=True, read_only=True)
    placa_patente = serializers.CharField(source='license_plate', label='placa_patente')
    marca = serializers.CharField(source='brand', label='marca')

    class Meta:
        model = Vehicle
        fields = ['placa_patente', 'marca', 'color', 'infracciones']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'email']
