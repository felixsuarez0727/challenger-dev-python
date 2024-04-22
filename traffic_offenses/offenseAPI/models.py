from django.db import models
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

class Offense(models.Model):
    plate_number = models.CharField(max_length=20, verbose_name="placa_patente")
    timestamp = models.TextField(verbose_name="timestamp")
    comments = models.TextField(verbose_name="comentarios")

    def __str__(self):
        return f"Infracción: {self.plate_number} - {self.timestamp}"

    class Meta:
        verbose_name = "infracción"
        verbose_name_plural = "infracciones"

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)