from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Q
from aplication.security.forms.grupos_modulos import GroupModulePermissionForm  # Asegúrate de importar el formulario correcto
from aplication.security.models import GroupModulePermission
from aplication.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin

class GroupModulePermissionListView( ListViewMixin, ListView):
    template_name = 'security/grupos_modulos/list.html'  # Asegúrate de tener el template adecuado para listar
    model = GroupModulePermission
    context_object_name = 'groupmodulepermissions'
    permission_required = 'view_groupmodulepermission'
    paginate_by = 12
    
    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1 is not None: 
            self.query.add(Q(group__name__icontains=q1) | Q(module__name__icontains=q1) , Q.OR) 
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('security:groupmodulepermission_create')
        return context

class GroupModulePermissionCreateView( CreateViewMixin, CreateView):
    model = GroupModulePermission
    template_name = 'security/grupos_modulos/form.html'  # Asegúrate de tener el template adecuado para el formulario
    form_class = GroupModulePermissionForm
    success_url = reverse_lazy('security:groupmodulepermission_list')
    permission_required = 'add_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Guardar Grupo Módulo Permiso'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        group_module_permission = self.object
        messages.success(self.request, f"Éxito al crear el grupo módulo permiso para el grupo {group_module_permission.group.name} y módulo {group_module_permission.module.name}.")
        return response

class GroupModulePermissionUpdateView( UpdateViewMixin, UpdateView):
    model = GroupModulePermission
    template_name = 'security/grupos_modulos/form.html'  # Asegúrate de tener el template adecuado para el formulario
    form_class = GroupModulePermissionForm
    success_url = reverse_lazy('security:groupmodulepermission_list')
    permission_required = 'change_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Grupo Módulo Permiso'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        group_module_permission = self.object
        messages.success(self.request, f"Éxito al actualizar el grupo módulo permiso para el grupo {group_module_permission.group.name} y módulo {group_module_permission.module.name}.")
        return response

class GroupModulePermissionDeleteView( DeleteViewMixin, DeleteView):
    model = GroupModulePermission
    template_name = 'security/delete.html'  # Asegúrate de tener el template adecuado para confirmar la eliminación
    success_url = reverse_lazy('security:groupmodulepermission_list')
    permission_required = 'delete_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Grupo Módulo Permiso'
        context['description'] = f"¿Desea eliminar lógicamente el grupo módulo permiso para el grupo: {self.object.group.name} y módulo: {self.object.module.name}?"
        context['back_url'] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente el grupo módulo permiso para el grupo {self.object.group.name} y módulo {self.object.module.name}."
        messages.success(self.request, success_message)
        # Realiza aquí la lógica para el borrado lógico, si aplica
        return super().delete(request, *args, **kwargs)
