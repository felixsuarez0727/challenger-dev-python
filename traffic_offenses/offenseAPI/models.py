from django.db import models
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from management.models import Vehicle

class Offense(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='infracciones', on_delete=models.CASCADE, verbose_name="license_plate")
    timestamp = models.TextField(verbose_name="timestamp")
    comments = models.TextField(verbose_name="comentarios")

    def __str__(self):
        return f"Infracción: {self.vehicle} - {self.timestamp}"

    class Meta:
        verbose_name = "infracción"
        verbose_name_plural = "infracciones"

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)