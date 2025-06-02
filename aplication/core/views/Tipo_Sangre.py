from django.urls import reverse_lazy
from aplication.core.forms.TipoSangre import TipoSangreForm
from aplication.core.models import TipoSangre
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class BloodTypeListView(ListView):
    template_name = "core/bloodtype/list.html"
    model = TipoSangre
    context_object_name = 'tipos_sangre'
    query = None
    paginate_by = 10
    
    def get_queryset(self):
        self.query = Q()
        q = self.request.GET.get('q')
        if q is not None: 
            self.query.add(Q(tipo__icontains=q), Q.OR) 
        return self.model.objects.filter(self.query).order_by('tipo')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de Tipos de Sangre"
        return context
    
class BloodTypeCreateView(CreateView):
    model = TipoSangre
    template_name = 'core/bloodtype/form.html'
    form_class = TipoSangreForm
    success_url = reverse_lazy('core:bloodtype_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar Tipo de Sangre'
        context['grabar'] = 'Grabar Tipo de Sangre'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        bloodtype = self.object
        save_audit(self.request, bloodtype, action='A')
        messages.success(self.request, f"Éxito al crear el tipo de sangre {bloodtype.tipo}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))
    
class BloodTypeUpdateView(UpdateView):
    model = TipoSangre
    template_name = 'core/bloodtype/form.html'
    form_class = TipoSangreForm
    success_url = reverse_lazy('core:bloodtype_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['title1'] = 'Modificar Tipo de Sangre'
        context['grabar'] = 'Actualizar Tipo de Sangre'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        bloodtype = self.object
        messages.success(self.request, f"Éxito al modificar el tipo de sangre {bloodtype.tipo}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al modificar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))
    
class BloodTypeDeleteView(DeleteView):
    model = TipoSangre
    success_url = reverse_lazy('core:bloodtype_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar Tipo de Sangre'
        context['description'] = f"¿Desea eliminar el tipo de sangre: {self.object.tipo}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar el tipo de sangre {self.object.tipo}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)
    
class BloodTypeDetailView(DetailView):
    model = TipoSangre
    
    def get(self, request, *args, **kwargs):
        bloodtype = self.get_object()
        data = {
            'id': bloodtype.id,
            'tipo': bloodtype.tipo,
            'descripcion': bloodtype.descripcion,
        }
        return JsonResponse(data)