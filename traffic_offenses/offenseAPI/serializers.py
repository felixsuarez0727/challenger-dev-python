from rest_framework import serializers
from .models import Offense

class OffenseSerializer(serializers.ModelSerializer):
    placa_patente = serializers.CharField(source='plate_number')
    timestamp = serializers.CharField()
    comentarios = serializers.CharField(source='comments')

    class Meta:
        model = Offense
        fields = ['placa_patente', 'timestamp', 'comentarios']
