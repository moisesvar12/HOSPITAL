from django.urls import path
from aplication.attention.views.medical_attention import AttentionCreateView, AttentionDetailView, AttentionListView, AttentionUpdateView
from aplication.core.views.home import HomeTemplateView
from aplication.core.views.patient import PatientCreateView, PatientDeleteView, PatientDetailView, PatientListView, PatientUpdateView
from aplication.attention.views.horario_atencion import HorarioAtencionCreateView,HorarioAtencionDeleteView,HorarioAtencionDetailView,HorarioAtencionListView,HorarioAtencionUpdateView
from aplication.attention.views.servicios_adicionales import ServiciosAdicionalesCreateView,ServiciosAdicionalesDeleteView,ServiciosAdicionalesDetailView,ServiciosAdicionalesListView,ServiciosAdicionalesUpdateView
from aplication.attention.views.certificate import CertificateCreateView,CertificateDeleteView,CertificateListView,CertificateUpdateView,CertificateDetailView
 
app_name='attention' # define un espacio de nombre para la aplicacion
urlpatterns = [
  # rutas de atenciones
  path('attention_list/',AttentionListView.as_view() ,name="attention_list"),
  path('attention_create/', AttentionCreateView.as_view(),name="attention_create"),
  path('attention_update/<int:pk>/', AttentionUpdateView.as_view(),name='attention_update'),
  path('attention_detail/<int:pk>/', AttentionDetailView.as_view(),name='attention_detail'),
  # path('patient_delete/<int:pk>/', PatientDeleteView.as_view(),name='patient_delete'),
       # Rutas de horarios de atención
  path('horario_list/', HorarioAtencionListView.as_view(), name="horario_list"),
  path('horario_create/', HorarioAtencionCreateView.as_view(), name="horario_create"),
  path('horario_update/<int:pk>/', HorarioAtencionUpdateView.as_view(), name='horario_update'),
  path('horario_detail/<int:pk>/', HorarioAtencionDetailView.as_view(), name='horario_detail'),
  path('horario_delete/<int:pk>/', HorarioAtencionDeleteView.as_view(), name='horario_delete'),
  # Nuevas rutas para servicios adicionales
  path('servicio_list/', ServiciosAdicionalesListView.as_view(), name="servicio_list"),
  path('servicio_create/', ServiciosAdicionalesCreateView.as_view(), name="servicio_create"),
  path('servicio_update/<int:pk>/', ServiciosAdicionalesUpdateView.as_view(), name='servicio_update'),
  path('servicio_detail/<int:pk>/', ServiciosAdicionalesDetailView.as_view(), name='servicio_detail'),
  path('servicio_delete/<int:pk>/', ServiciosAdicionalesDeleteView.as_view(), name='servicio_delete'),
# Certificados URLs
  path('certificates/', CertificateListView.as_view(), name='certificate_list'),
  path('certificate/create/', CertificateCreateView.as_view(), name='certificate_create'),
  path('certificate/update/<int:pk>/', CertificateUpdateView.as_view(), name='certificate_update'),
  path('certificate/delete/<int:pk>/', CertificateDeleteView.as_view(), name='certificate_delete'),
  path('certificate/detail/<int:pk>/', CertificateDetailView.as_view(), name='certificate_detail'),
  

]