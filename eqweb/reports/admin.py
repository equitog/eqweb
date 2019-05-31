from django.contrib import admin

# Register your models here.
from .models import Servicio, Subarea, Cuenta

admin.site.register(Servicio)
admin.site.register(Subarea)
admin.site.register(Cuenta)
