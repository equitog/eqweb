from django.db import models
from django.urls import reverse #Se utiliza para generar URL invirtiendo los patrones de URL

# Create your models here.
class Servicio(models.Model):

    id_servicio = models.AutoField(primary_key=True)
    name_servicio = models.CharField(max_length=100, null=False, blank=False, help_text="Ingrese el nombre del servicio.")
    date_since = models.DateField(null=False, blank=False)
    date_until = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        (0, 'Inactivo'),
        (1, 'Activo')
    )

    deactivate_servicio = models.BooleanField(default=1, choices=LOAN_STATUS, blank=False, help_text="Estado del servicio")

    def __str__(self):
        """
        String que representa al objeto servicio.
        """
        return self.name_servicio

class Subarea(models.Model):
    """ Modelo que repesenta una subarea """

    id_subarea = models.AutoField(primary_key=True)
    name_subarea = models.CharField(max_length=100, help_text="Ingrese el nombre de la subarea.")
    date_since = models.DateField(null=False, blank=False)
    date_until = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        (0, 'Inactivo'),
        (1, 'Activo'),
    )

    deactivate_subarea = models.BooleanField(choices=LOAN_STATUS, blank=True, default=1, help_text="Estado de la subarea")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administracion)
        """
        return self.name_subarea

class Cuenta(models.Model):

    id_cuenta = models.AutoField(primary_key=True)
    name_cuenta = models.CharField(max_length=100, null=False, blank=False, help_text="Ingrese nombre de la cuenta")
    date_since = models.DateField(null=False, blank=False)
    date_until = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        (0, 'Inactivo'),
        (1, 'Activo'),
    )

    deactivate_cuenta = models.BooleanField(default=1, choices=LOAN_STATUS, blank=True, help_text="Estado de la cuenta")

    def __str__(self):
        """
        String que representa al objeto cuenta.
        """
        return '{cuenta}'.format(cuenta=self.name_cuenta)

class Reporte(models.Model):

    id_report = models.AutoField(primary_key=True)
    name_report = models.CharField(max_length=100, null=False, blank=False, help_text="Ingrese nombre del reporte.")
    date_since = models.DateField(null=False, blank=False, help_text="Ingrese fecha de inicio de actividad")
    date_until = models.DateField(null=True, blank=True, help_text="Ingrese fecha de fin de actividad")
    LOAN_STATUS = (
        (0, 'Inactivo'),
        (1, 'Activo'),
    )
    status_report = models.BooleanField(null=False, blank=False, choices=LOAN_STATUS)
    id_cuenta = models.ForeignKey(Cuenta, on_delete=models.SET_NULL, null=True, blank=True, help_text="Ingrese nombre de la cuenta.")
    id_subarea = models.ForeignKey(Subarea, on_delete=models.SET_NULL, null=True, blank=True,help_text="Ingrese nombre de la sub-area")
    id_servicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True, blank=True,help_text="Ingrese Nombre del servicio")

    def __str__(self):
        return '{reports}'.format(reports=self.name_report)

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular
        """
        return reverse('reporte-detail', args=[str(self.id_report)])

    # def display_subarea(self):
    #    """
    #   Crea una cadena para la subarea. Este es requerido para mostrar subarea en el Admin
    #    """
    #    return ', '.join([ id_subarea.name_subarea for id_subarea in self.id_subarea.all()[:3] ])
    # display_subarea.short_description = 'Subarea'