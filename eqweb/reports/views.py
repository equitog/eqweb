from django.shortcuts import render
from .models import Servicio, Subarea, Cuenta, Reporte
# Create your views here.
def index(request):
    """
    Funcion vista para la pagina de inicio del sitio.
    """
    #Generar contadores de algunos de los objetos pinricpales
    num_reports = Reporte.objects.all().count()
    num_cuentas = Cuenta.objects.all().count()
    num_subarea = Subarea.objects.all().count()
    num_servicio = Servicio.objects.all().count()
    # Cuentas Activas (status = 1)
    num_activos = Cuenta.objects.filter(deactivate_cuenta__exact=1).count()

    # Renderizar la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_reports': num_reports,
                 'num_cuentas': num_cuentas,
                 'num_subarea': num_subarea,
                 'num_servicio': num_servicio,
                 'num_activos': num_activos},
    )