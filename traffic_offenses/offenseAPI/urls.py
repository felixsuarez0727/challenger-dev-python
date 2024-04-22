from django.urls import path
from .views import generate_report, upload_offense, generate_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('generar-token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('cargar_infraccion', upload_offense, name='cargar_infraccion'),
    path('generar_reporte', generate_report, name='generar_reporte'),
]
