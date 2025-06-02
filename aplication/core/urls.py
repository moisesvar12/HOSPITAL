from django.urls import path
from aplication.core.views.home import HomeTemplateView
from aplication.core.views.patient import PatientCreateView, PatientDeleteView, PatientDetailView, PatientListView, PatientUpdateView
from aplication.core.views.Tipo_Sangre import BloodTypeCreateView,BloodTypeDeleteView,BloodTypeDetailView,BloodTypeListView,BloodTypeUpdateView
from aplication.core.views.doctor import DoctorCreateView, DoctorDeleteView,DoctorListView,DoctorUpdateView,DoctorDetailView
from aplication.core.views.especialidad import EspecialidadCreateView,EspecialidadDeleteView,EspecialidadDetailView,EspecialidadListView,EspecialidadUpdateView
from aplication.core.views.examen import ExamenCreateView, ExamenDeleteView, ExamenDetailView, ExamenListView, ExamenUpdateView
from aplication.core.views.diagnostic import DiagnosticListView,DiagnosticCreateView,  DiagnosticUpdateView, DiagnosticDeleteView, DiagnosticDetailView 
from aplication.core.views.Auditoria import AuditoriaListView, AuditoriaDetailView
from aplication.core.views.marcamedicamento import MarcaMedicamentoCreateView,MarcaMedicamentoDeleteView,MarcaMedicamentoDetailView,MarcaMedicamentoListView,MarcaMedicamentoUpdateView
from aplication.core.views.medicamento import MedicamentoCreateView,MedicamentoDeleteView,MedicamentoDetailView,MedicamentoListView,MedicamentoUpdateView
from aplication.core.views.tipomedicamento import TipoMedicamentoDeleteView,TipoMedicamentoDetailView,TipoMedicamentoListView,TipoMedicamentotUpdateView,TipomedicamentoCreateView
from aplication.core.views.DashboardView import DashboardView
from aplication.attention.views.CitaMedica import CitaMedicaCreateView,CitaMedicaDeleteView,CitaMedicaDetailView,CitaMedicaListView,CitaMedicaUpdateView
from aplication.core.views.CrudCargo import CargoCreateView,CargoDeleteView,CargoDetailView,CargoListView,CargoUpdateView
from aplication.core.views.empleado import EmpleadoCreateView,EmpleadoDeleteView,EmpleadoDetailView,EmpleadoListView,EmpleadoUpdateView
from aplication.core.views.FichaClinica import FichaClinicaCreateView,FichaClinicaDeleteView,FichaClinicaDetailView,FichaClinicaListView,FichaClinicaUpdateView


app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
  # ruta principal
  path('', HomeTemplateView.as_view(),name='home'),
  # rutas doctores VBF
  # path('doctor_list/', views.doctor_List,name="doctor_list"),
  # path('doctor_create/', views.doctor_create,name="doctor_create"),
  # path('doctor_update/<int:id>/', views.doctor_update,name='doctor_update'),
  # path('doctor_delete/<int:id>/', views.doctor_delete,name='doctor_delete'),
  # rutas doctores VBC
  path('patient_list/',PatientListView.as_view() ,name="patient_list"),
  path('patient_create/', PatientCreateView.as_view(),name="patient_create"),
  path('patient_update/<int:pk>/', PatientUpdateView.as_view(),name='patient_update'),
  path('patient_delete/<int:pk>/', PatientDeleteView.as_view(),name='patient_delete'),
  path('patient_detail/<int:pk>/', PatientDetailView.as_view(),name='patient_detail'),
  # Tipo de Sangre URLS
  path('tipos_sangre/', BloodTypeListView.as_view(), name='bloodtype_list'),
  path('tipos_sangre/nuevo/', BloodTypeCreateView.as_view(), name='bloodtype_create'),
  path('tipos_sangre/editar/<int:pk>/', BloodTypeUpdateView.as_view(), name='bloodtype_update'),
  path('tipos_sangre/eliminar/<int:pk>/', BloodTypeDeleteView.as_view(), name='bloodtype_delete'),
  path('tipos_sangre/detalle/<int:pk>/', BloodTypeDetailView.as_view(), name='bloodtype_detail'),
  # Doctor Urls
  path('doctors/', DoctorListView.as_view(), name='doctor_list'),
  path('doctor/create/', DoctorCreateView.as_view(), name='doctor_create'),
  path('doctor/update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
  path('doctor/delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),
  path('doctor_detail/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
  # Especialidades URLS
  path('especialidades/', EspecialidadListView.as_view(), name='especialidad_list'),
  path('especialidad/create/', EspecialidadCreateView.as_view(), name='especialidad_create'),
  path('especialidad/update/<int:pk>/', EspecialidadUpdateView.as_view(), name='especialidad_update'),
  path('especialidad/delete/<int:pk>/', EspecialidadDeleteView.as_view(), name='especialidad_delete'),
  path('especialidad/detail/<int:pk>/', EspecialidadDetailView.as_view(), name='especialidad_detail'),
  #############
  path('examenes/', ExamenListView.as_view(), name='examen_list'),  # Listado de exámenes
  path('examenes/nuevo/', ExamenCreateView.as_view(), name='examen_create'),  # Crear examen
  path('examenes/<int:pk>/editar/', ExamenUpdateView.as_view(), name='examen_update'),  # Editar examen
  path('examenes/<int:pk>/eliminar/', ExamenDeleteView.as_view(), name='examen_delete'),  # Eliminar examen
  path('examenes/<int:pk>/', ExamenDetailView.as_view(), name='examen_detail'),  # Detalle examen (JSON)
  path('diagnostic_list/', DiagnosticListView.as_view(), name="diagnostic_list"),# Listar diagnósticos
  path('diagnostic_create/', DiagnosticCreateView.as_view(), name="diagnostic_create"),# Crear diagnóstico
  path('diagnostic_update/<int:pk>/', DiagnosticUpdateView.as_view(), name='diagnostic_update'),# Actualizar diagnóstico
  path('diagnostic_delete/<int:pk>/', DiagnosticDeleteView.as_view(), name='diagnostic_delete'), # Eliminar diagnóstico
  path('diagnostic_detail/<int:pk>/', DiagnosticDetailView.as_view(), name='diagnostic_detail'), # Ver detalle de diagnóstico
  path('auditoria/', AuditoriaListView.as_view(), name='auditoria_list'),  # Listar registros de auditoría
  path('auditoria/<int:pk>/', AuditoriaDetailView.as_view(), name='auditoria_detail'),  # Detalles de auditoría
  #Tipo medicamentos
  path('tipom_list/', TipoMedicamentoListView.as_view(), name="tipom_list"),
  path('tipom_create/', TipomedicamentoCreateView.as_view(), name="tipom_create"),
  path('tipom_update/<int:pk>/', TipoMedicamentotUpdateView.as_view(), name="tipom_update"),
  path('tipom_delete/<int:pk>/', TipoMedicamentoDeleteView.as_view(), name="tipom_delete"),
  path('tipom_detail/<int:pk>/', TipoMedicamentoDetailView.as_view(), name='tipom_detail'),
  #Marca Medicamento
  path('marca_list/', MarcaMedicamentoListView.as_view(), name="marca_list"),
  path('marca_create/', MarcaMedicamentoCreateView.as_view(), name="marca_create"),
  path('marca_update/<int:pk>/',MarcaMedicamentoUpdateView.as_view(), name='marca_update'),
  path('marca_delete/<int:pk>/', MarcaMedicamentoDeleteView.as_view(), name='marca_delete'),
  path('marca_detail/<int:pk>/', MarcaMedicamentoDetailView.as_view(), name='marca_detail'),
  #Medicamentos
  path('medicamento_list/', MedicamentoListView.as_view(), name="medicamento_list"),
  path('medicamento_create/', MedicamentoCreateView.as_view(), name="medicamento_create"),
  path('medicamento_update/<int:pk>/',MedicamentoUpdateView.as_view(), name='medicamento_update'),
  path('medicamento_delete/<int:pk>/',MedicamentoDeleteView.as_view(), name='medicamento_delete'),
  path('medicamento_detail/<int:pk>/', MedicamentoDetailView.as_view(), name='medicamento_detail'),
  ##ruta de las opciones
  path('dashboard/', DashboardView.as_view(), name='dashboard'),
  #ruta de citasmedicas
  path('citas/', CitaMedicaListView.as_view(), name='cita_list'),
  path('<int:pk>/', CitaMedicaDetailView.as_view(), name='cita_detail'),
  path('citas2/nueva/', CitaMedicaCreateView.as_view(), name='cita_create'),
  path('citas3/<int:pk>/editar/', CitaMedicaUpdateView.as_view(), name='cita_edit'),
  path('citas4/<int:pk>/eliminar/', CitaMedicaDeleteView.as_view(), name='cita_delete'),
  #Ruta Empleado
  path('empleado_list/',EmpleadoListView.as_view() ,name="empleado_list"),
  path('empleado_create/', EmpleadoCreateView.as_view(),name="empleado_create"),
  path('empleado_update/<int:pk>/', EmpleadoUpdateView.as_view(),name='empleado_update'),
  path('empleado_delete/<int:pk>/', EmpleadoDeleteView.as_view(),name='empleado_delete'),
  path('empleado_detail/<int:pk>/', EmpleadoDetailView.as_view(),name='empleado_detail'), 
    #RUTA Especialidad
  path('Cargo/', CargoListView.as_view(), name='listarcargo'),
  path('Cargocrear/', CargoCreateView.as_view(), name='crearcargo'),
  path('<int:pk>', CargoDetailView.as_view(), name='detallecargo'),
  path('Cargoedit/<int:pk>/editar/', CargoUpdateView.as_view(), name='editarcargo'),
  path('Cargodelete/<int:pk>/eliminar/', CargoDeleteView.as_view(), name='eliminarcargo'),
  #### fichas
  path('fichas/', FichaClinicaListView.as_view(), name='lista_fichas'),
  path('fichas/<int:pk>/', FichaClinicaDetailView.as_view(), name='detalle_ficha'),
  path('fichas/nueva/', FichaClinicaCreateView.as_view(), name='crear_ficha'),
  path('fichas/<int:pk>/editar/', FichaClinicaUpdateView.as_view(), name='editar_ficha'),
  path('fichas/<int:pk>/eliminar/', FichaClinicaDeleteView.as_view(), name='eliminar_ficha'),
  
]
