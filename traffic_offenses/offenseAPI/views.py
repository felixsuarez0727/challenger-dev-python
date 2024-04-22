from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import OffenseSerializer
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from management.models import Officer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_offense(request):
    if request.method == 'POST':
        serializer = OffenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def generate_token(request):
    identification_number = request.data.get('identification_number')
    
    if not identification_number:
        return Response({'error': 'Identification number is required'}, status=400)

    # Intentamos obtener el objeto Officer con el número de identificación proporcionado
    try:
        officer = get_object_or_404(Officer, identification_number=identification_number)
    except officer.DoesNotExist:
        return Response({'error': 'Invalid identification number'}, status=404)
    
    # Generamos o obtenemos el token asociado al oficial
    token, created = Token.objects.get_or_create(user=officer.identification_number)

    return Response({'token': token.key},status=status.HTTP_200_OK)
