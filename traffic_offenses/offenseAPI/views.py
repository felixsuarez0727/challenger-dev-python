from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import OffenseSerializer, VehicleSerializer
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from management.models import Officer, Person, Vehicle

@api_view(['POST']) 
@permission_classes([IsAuthenticated])   
def upload_offense(request):
    placa = request.data.get('placa_patente')
    vehicle = Vehicle.objects.filter(license_plate=placa).first()
    if not vehicle:
        return Response({'error': 'Vehículo no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    print(f"vehiculo {vehicle}")
    
    data = {
        'vehicle': vehicle.license_plate,
        'timestamp': request.data.get('timestamp'),
        'comentarios': request.data.get('comentarios')
    }
    serializer = OffenseSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([AllowAny])
def generate_report(request):
    email = request.query_params.get('email')
    if not email:
        return Response({"error": "Se requiere un parámetro de correo electrónico"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    person = get_object_or_404(Person, email=email)
    vehicles = person.vehicle_set.all()

    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def generate_token(request):
    identification_number = request.data.get('identification_number')
    
    if not identification_number:
        return Response({'error': 'Identification number is required'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    try:
        officer = get_object_or_404(Officer, identification_number=identification_number)
    except officer.DoesNotExist:
        return Response({'error': 'Invalid identification number'}, status=status.HTTP_404_NOT_FOUND)
    
    token, created = Token.objects.get_or_create(user=officer.identification_number)

    return Response({'token': token.key},status=status.HTTP_200_OK)
