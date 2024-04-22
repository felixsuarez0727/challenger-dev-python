from rest_framework import serializers
from management.models import Officer, Vehicle, Person
from .models import Offense
from rest_framework.authtoken.models import Token

class OffenseSerializer(serializers.ModelSerializer):
    placa_patente = serializers.CharField(source='plate_number')
    timestamp = serializers.CharField()
    comentarios = serializers.CharField(source='comments')

    class Meta:
        model = Offense
        fields = ['placa_patente', 'timestamp', 'comentarios']

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['license_plate', 'brand', 'color', 'owner']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'email']

class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = ['name', 'identification_number']

class TokenSerializer(serializers.ModelSerializer):
    officer = OfficerSerializer()

    class Meta:
        model = Token
        fields = ['key', 'officer']

    def create(self, validated_data):
        officer_data = validated_data.pop('officer')
        officer = Officer.objects.create(**officer_data)
        token = Token.objects.create(user=officer)
        return token
