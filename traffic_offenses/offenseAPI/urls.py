from django.urls import path
from .views import upload_offense

urlpatterns = [
    path('cargar_infraccion/', upload_offense, name='cargar_infraccion'),
]
