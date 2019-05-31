from django.db import models
from django.urls import reverse #Se utiliza para generar URL invirtiendo los patrones de URL

# Create your models here.
class Servicio(models.Model):

    id_servicio = models.IntegerField(primary_key=True)
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

    id_subarea = models.IntegerField(primary_key=True)
    name_subarea = models.CharField(max_length=100, help_text="Ingrese el nombre de la subarea.")
    date_since = models.DateField(null=False, blank=False)
    date_until = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        (0, 'Inactivo'),
        (1, 'Activo'),
    )

    deactivate_subarea = models.BooleanField(choices=LOAN_STATUS, blank=True, default=1, help_text="Estado de la subarea")
    id_servicio = models.ForeignKey(Servicio.id_servicio, on_delete=models.SET_NULL, help_text="Ingrese servicio para la subarea")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administracion)
        """
        return self.name_subarea, self.id_subarea

class Cuenta(models.Model):

    id_cuenta = models.IntegerField(primary_key=True)
    name_cuenta = models.CharField(max_length=100, null=False, blank=False, help_text="Ingrese nombre de la cuenta")
    date_since = models.DateField(null=False, blank=False)
    data_until = models.DateField(null=True, blank=True)
    deactivate_cuenta = models.BooleanField(default=0)
    id_subarea = models.ForeignKey(Subarea, on_delete=models.SET_NULL, help_text="Ingrese la subarea para la cuenta")

    def __str__(self):
        """
        String que representa al objeto cuenta.
        """
        return '{cuenta}'.format(cuenta=self.name_cuenta)
    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular
        """
        return reverse('cuenta-detail', args=[str(self.id_cuenta)])