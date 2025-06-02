from django.urls import reverse_lazy
from aplication.core.forms.medicamento import MedicamentoForm
from aplication.core.models import Medicamento
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from doctor.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, UpdateViewMixin
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class MedicamentoListView(LoginRequiredMixin,ListViewMixin,ListView):
    template_name = "core/medicamento/list.html"
    model = Medicamento
    context_object_name = 'medicamentos'
    query = None
    paginate_by = 10
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q') # ver
        
        if q1 is not None: 
            self.query.add(Q(nombre__icontains=q1), Q.OR) 
        return self.model.objects.filter(self.query).order_by('nombre')
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = "Medical"
    #     context['title1'] = "Consulta de Medicamentos"
    #     return context
    
class MedicamentoCreateView(LoginRequiredMixin,CreateViewMixin, CreateView):
    model = Medicamento
    template_name = 'core/medicamento/form.html'
    form_class = MedicamentoForm
    success_url = reverse_lazy('core:medicamento_list')
    # permission_required = 'add_supplier' # en PermissionMixn se verfica si un grupo tiene el permiso

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Crear Medicamento?'
        context['grabar'] = 'Grabar Medicamento'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # print("entro al form_valid")
        response = super().form_valid(form)
        medicamento = self.object
        save_audit(self.request, medicamento, action='A')
        messages.success(self.request, f"Éxito al crear el medicamento {medicamento.nombre}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class MedicamentoUpdateView(LoginRequiredMixin,UpdateViewMixin,UpdateView):
    model = Medicamento
    template_name = 'core/medicamento/form.html'
    form_class = MedicamentoForm
    success_url = reverse_lazy('core:medicamento_list')
    # permission_required = 'change_patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Medicamento'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        medicamento = self.object
        save_audit(self.request, medicamento, action='M')
        messages.success(self.request, f"Éxito al Modificar el medicamento {medicamento.nombre}.")
        print("mande mensaje")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al Modificar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class MedicamentoDeleteView(LoginRequiredMixin,DeleteViewMixin,DeleteView):
    model = Medicamento
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy('core:medicamento_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar medicamento'
        context['description'] = f"¿Desea Eliminar el medicamento: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente al medicamento {self.object.name}."
        messages.success(self.request, success_message)
        # Cambiar el estado de eliminado lógico
        # self.object.deleted = True
        # self.object.save()
        return super().delete(request, *args, **kwargs)
    
class MedicamentoDetailView(LoginRequiredMixin,DetailView):
    model = Medicamento
    
    def get(self, request, *args, **kwargs):
        medicamento = self.get_object()
        data = {
            'id': medicamento.id,
            'nombre': medicamento.nombre,
            'descripcion': medicamento.descripcion,
            'concentracion': medicamento.concentracion,
            'cantidad': medicamento.cantidad,
            'precio': medicamento.precio,
            'foto': medicamento.get_image(),
            'comercial': medicamento.comercial,
            # Añade más campos según tu modelo
        }
        return JsonResponse(data)