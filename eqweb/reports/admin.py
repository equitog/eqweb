from django.contrib import admin

# Register your models here.
from .models import Servicio, Subarea, Cuenta, Reporte

#admin.site.register(Servicio)
#admin.site.register(Subarea)
#admin.site.register(Cuenta)
@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('name_cuenta', 'date_since', 'date_until', 'deactivate_cuenta')
    list_filter = ('name_cuenta', 'deactivate_cuenta')


@admin.register(Subarea)
class SubareaAdmin(admin.ModelAdmin):
    list_display = ('name_subarea', 'date_since', 'date_until', 'deactivate_subarea')
    fieldsets = (
        ('Sub-Area', {
            'fields': ['name_subarea']
        }),
        ('Estado Sub-Area', {
            'fields': ['date_since', 'date_until', 'deactivate_subarea']
        }),
    )
    #fields = ['name_subarea', ('date_since', 'date_until', 'deactivate_subarea')]


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('name_servicio', 'date_since', 'date_until', 'deactivate_servicio')
    fieldsets = (
        ('Servicio', {
            'fields': ['name_servicio']
        }),
        ('Estado Servicio', {
            'fields': ['date_since', 'date_until', 'deactivate_servicio']
        })
    )
@admin.register(Reporte)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ('name_report', 'date_since', 'date_until', 'status_report', 'id_cuenta', 'id_subarea', 'id_servicio')
    fieldsets = (
        ('Reporte', {
            'fields': ['name_report']
        }),
        ('Estado del Reporte', {
            'fields': ['date_since', 'date_until', 'status_report']
        }),
        ('Derechos de reporte', {
            'fields': ['id_cuenta', 'id_subarea', 'id_servicio']
        })
    )
