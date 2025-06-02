from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from aplication.security.forms.module import ModuleForm
from aplication.security.models import Module
from aplication.security.mixins.mixins import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin
from django.db.models import Q

class ModuleListView( ListViewMixin, ListView):
    template_name = 'security/modulos/list.html'  # Asegúrate de tener el template adecuado para listar modules
    model = Module
    context_object_name = 'modules'
    permission_required = 'view_module'
    
    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1 is not None: 
            self.query.add(Q(name__icontains=q1) | Q(description__icontains=q1), Q.OR) 
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('security:module_create')
        return context
class ModuleCreateView( CreateViewMixin, CreateView):
    model = Module
    template_name = 'security/modulos/form.html'  # Asegúrate de tener el template adecuado para el formulario de module
    form_class = ModuleForm
    success_url = reverse_lazy('security:module_list')
    permission_required = 'add_module'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Guardar Módulo'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        module = self.object
        messages.success(self.request, f"Éxito al crear el módulo {module.name}.")
        return response
class ModuleUpdateView( UpdateViewMixin, UpdateView):
    model = Module
    template_name = 'security/modulos/form.html'  # Asegúrate de tener el template adecuado para el formulario de module
    form_class = ModuleForm
    success_url = reverse_lazy('security:module_list')
    permission_required = 'change_module'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Módulo'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        module = self.object
        messages.success(self.request, f"Éxito al actualizar el módulo {module.name}.")
        return response
class ModuleDeleteView( DeleteViewMixin, DeleteView):
    model = Module
    template_name = 'security/delete.html'  # Asegúrate de tener el template adecuado para confirmar la eliminación
    success_url = reverse_lazy('security:module_list')
    permission_required = 'delete_module'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Módulo'
        context['description'] = f"¿Desea eliminar lógicamente el módulo: {self.object.name}?"
        context['back_url'] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente el módulo {self.object.name}."
        messages.success(self.request, success_message)
        # Realiza aquí la lógica para el borrado lógico, si aplica
        return super().delete(request, *args, **kwargs)
