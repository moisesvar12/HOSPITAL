from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from aplication.core.forms.examen import ExamenForm
from aplication.core.models import ExamenMedico
from doctor.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, UpdateViewMixin
from doctor.utils import save_audit

class ExamenListView(LoginRequiredMixin, ListViewMixin, ListView):
    template_name = "core/examen/list.html"
    model = ExamenMedico
    context_object_name = 'examenes'
    paginate_by = 10  # Paginación



# Vista para crear un examen
class ExamenCreateView(LoginRequiredMixin, CreateViewMixin, CreateView):
    model = ExamenMedico
    template_name = 'core/examen/form.html'
    form_class = ExamenForm
    success_url = reverse_lazy('core:examen_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Examen'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        examen = self.object
        save_audit(self.request, examen, action='A')  # Guardar auditoría
        messages.success(self.request, f"Éxito al crear el examen de {examen.paciente.nombre_completo}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

# Vista para actualizar un examen
class ExamenUpdateView(LoginRequiredMixin, UpdateViewMixin, UpdateView):
    model = ExamenMedico
    template_name = 'core/examen/form.html'
    form_class = ExamenForm
    success_url = reverse_lazy('core:examen_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Examen'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        examen = self.object
        save_audit(self.request, examen, action='M')  # Acción M = Modificar
        messages.success(self.request, f"Éxito al modificar el examen de {examen.paciente.nombre_completo}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al modificar el examen. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

# Vista para eliminar un examen
class ExamenDeleteView(LoginRequiredMixin, DeleteViewMixin, DeleteView):
    model = ExamenMedico
    success_url = reverse_lazy('core:examen_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Examen'
        context['description'] = f"¿Desea eliminar el examen de {self.object.paciente.nombre_completo}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente el examen de {self.object.paciente.nombre_completo}."
        messages.success(self.request, success_message)
        # Lógica de eliminación (puedes agregar eliminación lógica aquí)
        # self.object.activo = False  # Dejar el examen como inactivo
        # self.object.save()
        
        return super().delete(request, *args, **kwargs)

# Vista para detallar un examen (en formato JSON)
class ExamenDetailView(LoginRequiredMixin, DetailView):
    model = ExamenMedico

    def get(self, request, *args, **kwargs):
        examen = self.get_object()
        data = {
            'id': examen.id,
            'fecha_examen': examen.fecha_examen,
            'resultado': examen.resultado,
            'diagnostico': examen.diagnostico,
            'medicamentos_recomendados': examen.medicamentos_recomendados,
            'comentarios': examen.comentarios,
            'tipo_examen': examen.tipo_examen,
            'observaciones': examen.observaciones,
            'paciente': examen.paciente.nombre_completo,  # Suponiendo que el modelo Paciente tiene este atributo
        }
        return JsonResponse(data)
