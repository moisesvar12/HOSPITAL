from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from aplication.core.models import FichaClinica
from django.contrib import messages

# Vista para listar las fichas clínicas
class FichaClinicaListView(ListView):
    model = FichaClinica
    template_name = 'core/fichas/lista_fichas.html'
    context_object_name = 'fichas_clinicas'

    def get_queryset(self):
        # Agregar un filtro si es necesario
        return FichaClinica.objects.filter(activo=True).order_by('-fecha_consulta')

# Vista para ver los detalles de una ficha clínica
class FichaClinicaDetailView(DetailView):
    model = FichaClinica
    template_name = 'core/fichas/detalle_ficha.html'
    context_object_name = 'ficha'

# Vista para crear una nueva ficha clínica
class FichaClinicaCreateView(CreateView):
    model = FichaClinica
    template_name = 'core/fichas/formulario_ficha.html'
    fields = ['paciente', 'doctor', 'motivo_consulta', 'diagnostico', 'tratamiento', 'notas']
    success_url = reverse_lazy('core:lista_fichas')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Ficha clínica creada con éxito.")
        return response

# Vista para editar una ficha clínica
class FichaClinicaUpdateView(UpdateView):
    model = FichaClinica
    template_name = 'core/fichas/formulario_ficha.html'
    fields = ['paciente', 'doctor', 'motivo_consulta', 'diagnostico', 'tratamiento', 'notas']
    success_url = reverse_lazy('core:lista_fichas')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Ficha clínica actualizada con éxito.")
        return response

# Vista para eliminar una ficha clínica
class FichaClinicaDeleteView(DeleteView):
    model = FichaClinica
    template_name = 'core/fichas/confirmar_eliminacion_ficha.html'
    success_url = reverse_lazy('core:lista_fichas')
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Ficha clínica eliminada con éxito.")
        return super().delete(request, *args, **kwargs)
