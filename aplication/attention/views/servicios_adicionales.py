from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.db.models import Q
from django.contrib import messages
from aplication.attention.models import ServiciosAdicionales
from aplication.attention.forms.servicios_forms import ServiciosAdicionalesForm  
from django.http import JsonResponse
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView



# List View
class ServiciosAdicionalesListView(LoginRequiredMixin, ListView):
    template_name = "attention/servicio_adicionales/list.html"
    model = ServiciosAdicionales
    context_object_name = 'servicios'
    
    def get_queryset(self):
        query = Q()
        nombre_servicio = self.request.GET.get('nombre_servicio')
        activo = self.request.GET.get('activo')
        
        if nombre_servicio:
            query.add(Q(nombre_servicio__icontains=nombre_servicio), Q.AND)
        if activo in ['True', 'False']:
            query.add(Q(activo=activo == 'True'), Q.AND)
        
        return self.model.objects.filter(query).order_by('nombre_servicio')
    

  # Si lo tienes

class ServiciosAdicionalesCreateView(LoginRequiredMixin, CreateView):
    model = ServiciosAdicionales
    form_class = ServiciosAdicionalesForm  # Si tienes formulario
    template_name = 'attention/servicio_adicionales/form.html'
    success_url = reverse_lazy('attention:servicio_list')  # Cambiar si es necesario

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Crear Servicio Adicional'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        servicio = self.object
        messages.success(self.request, f"Servicio adicional '{servicio.nombre_servicio}' creado con éxito.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))



class ServiciosAdicionalesUpdateView(LoginRequiredMixin, UpdateView):
    model = ServiciosAdicionales
    form_class = ServiciosAdicionalesForm  # Si tienes formulario
    template_name = 'attention/servicio_adicionales/form.html'
    success_url = reverse_lazy('attention:servicio_list')  # Cambiar si es necesario

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Servicio Adicional'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        servicio = self.object
        messages.success(self.request, f"Servicio adicional '{servicio.nombre_servicio}' actualizado con éxito.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al actualizar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))
    
class ServiciosAdicionalesDeleteView(LoginRequiredMixin, DeleteView):
    model = ServiciosAdicionales
    success_url = reverse_lazy('attention:servicio_list')  # Cambiar si es necesario

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Servicio Adicional'
        context['description'] = f"¿Desea eliminar el servicio adicional '{self.object.nombre_servicio}'?"
        context['back_url'] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Servicio adicional '{self.object.nombre_servicio}' eliminado con éxito."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)




class ServiciosAdicionalesDetailView(LoginRequiredMixin, DetailView):
    model = ServiciosAdicionales

    def get(self, request, *args, **kwargs):
        servicio = self.get_object()
        data = {
            'id': servicio.id,
            'nombre_servicio': servicio.nombre_servicio,
            'costo_servicio': str(servicio.costo_servicio),
            'descripcion': servicio.descripcion,
            'activo': servicio.activo,
        }
        return JsonResponse(data)
