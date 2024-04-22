from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Person, Vehicle, Officer

class OfficerAdmin(UserAdmin):
    model = Officer
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('identification_number',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'identification_number'),
        }),
    )

admin.site.register(Person)
admin.site.register(Vehicle)
admin.site.register(Officer, OfficerAdmin)

