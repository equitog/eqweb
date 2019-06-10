from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reports/$', views.ReportListView.as_view(), name='reporte'),
    url(r'^reporte/(?P<pk>\d+)$', views.ReportDetailView.as_view(), name='reporte-detail'),
]