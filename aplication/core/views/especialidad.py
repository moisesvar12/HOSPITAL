from django.urls import reverse_lazy
from aplication.core.forms.especialidad import EspecialidadForm
from aplication.core.models import Especialidad
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q

class EspecialidadListView(ListView):
    template_name = "core/especialidades/list.html"
    model = Especialidad
    context_object_name = 'especialidades'
    query = None
    paginate_by = 2
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q')  # búsqueda por nombre o descripción
        if q1 is not None:
            self.query.add(Q(nombre__icontains=q1), Q.OR)
            self.query.add(Q(descripcion__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de Especialidades"
        return context
    
class EspecialidadCreateView(CreateView):
    model = Especialidad
    template_name = 'core/especialidades/form.html'
    form_class = EspecialidadForm
    success_url = reverse_lazy('core:especialidad_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar Información de Especialidad'
        context['grabar'] = 'Grabar Especialidad'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        especialidad = self.object
        messages.success(self.request, f"Éxito al crear la especialidad {especialidad.nombre}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

class EspecialidadUpdateView(UpdateView):
    model = Especialidad
    template_name = 'core/especialidades/form.html'
    form_class = EspecialidadForm
    success_url = reverse_lazy('core:especialidad_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Modificar Información de Especialidad'
        context['grabar'] = 'Actualizar Especialidad'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        especialidad = self.object
        messages.success(self.request, f"Éxito al modificar la especialidad {especialidad.nombre}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al modificar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

class EspecialidadDeleteView(DeleteView):
    model = Especialidad
    success_url = reverse_lazy('core:especialidad_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar Especialidad'
        context['description'] = f"¿Desea eliminar la especialidad: {self.object.nombre}?"
        context['back_url'] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False
        self.object.save()
        success_message = f"Éxito al eliminar lógicamente la especialidad {self.object.nombre}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)

class EspecialidadDetailView(DetailView):
    model = Especialidad
    
    def get(self, request, *args, **kwargs):
        especialidad = self.get_object()
        data = {
            'id': especialidad.id,
            'nombre': especialidad.nombre,
            'descripcion': especialidad.descripcion,
            'activo': especialidad.activo,
        }
        return JsonResponse(data)