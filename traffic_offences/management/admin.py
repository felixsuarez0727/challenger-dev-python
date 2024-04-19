from django.contrib import admin
from .models import Person, Vehicle, Officer

admin.site.register(Person)
admin.site.register(Vehicle)
admin.site.register(Officer)
