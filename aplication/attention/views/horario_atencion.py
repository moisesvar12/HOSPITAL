from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, UpdateViewMixin
from doctor.utils import save_audit
from aplication.attention.models import HorarioAtencion  # Cambiado de core a attention
from aplication.attention.forms.horario_forms import HorarioAtencionForm  # Cambiado de core a attention

# List View
class HorarioAtencionListView(LoginRequiredMixin, ListViewMixin, ListView):
    template_name = "attention/horario_atencion/list.html"  # Cambiado de core a attention
    model = HorarioAtencion
    context_object_name = 'horarios'
    
    def get_queryset(self):
        query = Q()
        dia = self.request.GET.get('dia')
        activo = self.request.GET.get('activo')
        
        if dia:
            query.add(Q(dia_semana__icontains=dia), Q.AND)
        if activo in ['True', 'False']:
            query.add(Q(activo=activo == 'True'), Q.AND)
        
        return self.model.objects.filter(query).order_by('dia_semana')

# Create View
class HorarioAtencionCreateView(LoginRequiredMixin, CreateViewMixin, CreateView):
    model = HorarioAtencion
    template_name = 'attention/horario_atencion/form.html'  # Cambiado de core a attention
    form_class = HorarioAtencionForm
    success_url = reverse_lazy('attention:horario_list')  # Cambiado namespace de core a attention

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Crear Horario'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        horario = self.object
        save_audit(self.request, horario, action='A')
        messages.success(self.request, f"Horario de atención creado con éxito: {horario.dia_semana}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

# Update View
class HorarioAtencionUpdateView(LoginRequiredMixin, UpdateViewMixin, UpdateView):
    model = HorarioAtencion
    template_name = 'attention/horario_atencion/form.html'  # Cambiado de core a attention
    form_class = HorarioAtencionForm
    success_url = reverse_lazy('attention:horario_list')  # Cambiado namespace de core a attention

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Horario'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        horario = self.object
        save_audit(self.request, horario, action='M')
        messages.success(self.request, f"Horario de atención actualizado con éxito: {horario.dia_semana}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al actualizar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

# Delete View
class HorarioAtencionDeleteView(LoginRequiredMixin, DeleteViewMixin, DeleteView):
    model = HorarioAtencion
    success_url = reverse_lazy('attention:horario_list')  # Cambiado namespace de core a attention

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Horario'
        context['description'] = f"¿Desea eliminar el horario de atención del día {self.object.dia_semana}?"
        context['back_url'] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Horario de atención eliminado con éxito: {self.object.dia_semana}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)

# Detail View
class HorarioAtencionDetailView(LoginRequiredMixin, DetailView):
    model = HorarioAtencion

    def get(self, request, *args, **kwargs):
        horario = self.get_object()
        data = {
            'id': horario.id,
            'dia_semana': horario.dia_semana,
            'hora_inicio': horario.hora_inicio,
            'hora_fin': horario.hora_fin,
            'intervalo_desde': horario.intervalo_desde,
            'intervalo_hasta': horario.intervalo_hasta,
            'activo': horario.activo,
        }
        return JsonResponse(data)
