from django.urls import reverse_lazy
from aplication.security.forms.menu import MenuForm
from aplication.security.models import Menu
from aplication.security.instance.menu_module import MenuModule
from aplication.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Q

class MenuListView(ListViewMixin, ListView):
    template_name = 'security/menu/list.html'
    model = Menu
    context_object_name = 'menus'
    permission_required = 'view_menu'
    
    def get_queryset(self):
        q1 = self.request.GET.get('q') # ver
        if q1 is not None: 
            self.query.add(Q(name__icontains=q1), Q.OR) 
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['permission_add'] = context['permissions'].get('add_supplier','')
        context['create_url'] = reverse_lazy('security:menu_create')
        return context
    
class MenuCreateView(CreateViewMixin, CreateView):
    model = Menu
    template_name = 'security/menu/form.html'
    form_class = MenuForm
    success_url = reverse_lazy('security:menu_list')
    permission_required = 'add_menu' # en PermissionMixn se verfica si un grupo tiene el permiso

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Menu'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        menu = self.object
        messages.success(self.request, f"Éxito al crear la Menu {menu.name}.")
        return response
    
class MenuUpdateView(UpdateViewMixin, UpdateView):
    model = Menu
    template_name = 'security/menu/form.html'
    form_class = MenuForm
    success_url = reverse_lazy('security:menu_list')
    permission_required = 'change_menu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Menu'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        menu = self.object
        messages.success(self.request, f"Éxito al actualizar la Menu {menu.name}.")
        return response
    
class MenuDeleteView(DeleteViewMixin, DeleteView):
    model = Menu
    template_name = 'security/delete.html'
    success_url = reverse_lazy('security:menu_list')
    permission_required = 'delete_menu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Menu'
        context['description'] = f"¿Desea Eliminar la Menu: {self.object.name}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente la Menu {self.object.name}."
        messages.success(self.request, success_message)
        # Cambiar el estado de eliminado lógico
        # self.object.deleted = True
        # self.object.save()
        return super().delete(request, *args, **kwargs)