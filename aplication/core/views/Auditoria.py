from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from aplication.security.models import AuditUser

# Vista para listar los registros de auditoría
class AuditoriaListView(LoginRequiredMixin, ListView):
    model = AuditUser
    template_name = 'core/auditoria/list.html'
    context_object_name = 'auditorias'  # El nombre de la variable que se pasa a la plantilla
    paginate_by = 10  # Puedes cambiar la cantidad de auditorías por página

    def get_queryset(self):
        # Puedes agregar filtros aquí si es necesario, por ejemplo, por usuario o fecha
        return AuditUser.objects.all()  # Recuperamos todas las auditorías
class AuditoriaDetailView(LoginRequiredMixin, DetailView):
    model = AuditUser
    template_name = 'core/auditoria/detail.html'
    context_object_name = 'auditoria'
