from django.urls import reverse_lazy
from aplication.core.forms.diagnostic import DiagnosticoForm  # Asegúrate de tener este formulario
from aplication.core.models import Diagnostico
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, UpdateViewMixin
from doctor.utils import save_audit

# Vista para listar diagnósticos
class DiagnosticListView(LoginRequiredMixin, ListViewMixin, ListView):
    template_name = "core/diagnostic/list.html"
    model = Diagnostico
    context_object_name = 'diagnosticos'

    def get_queryset(self):
        q1 = self.request.GET.get('q')  # Búsqueda
        category = self.request.GET.get('category')
        query = Q()

        if q1:
            query.add(Q(codigo__icontains=q1), Q.OR)  # Filtro por código
            query.add(Q(descripcion__icontains=q1), Q.OR)  # Filtro por descripción

        if category:  # Filtro por categoría (no disponible en tu modelo, pero se deja como ejemplo)
            query.add(Q(datos_adicionales__icontains=category), Q.AND)

        return self.model.objects.filter(query).order_by('codigo')

# Vista para crear un diagnóstico
class DiagnosticCreateView(LoginRequiredMixin, CreateViewMixin, CreateView):
    model = Diagnostico
    template_name = 'core/diagnostic/form.html'
    form_class = DiagnosticoForm  # Asegúrate de tener este formulario
    success_url = reverse_lazy('core:diagnostic_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Diagnóstico'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        diagnostic = self.object
        save_audit(self.request, diagnostic, action='A')
        messages.success(self.request, f"Éxito al crear el diagnóstico {diagnostic.codigo} - {diagnostic.descripcion}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

# Vista para actualizar un diagnóstico
class DiagnosticUpdateView(LoginRequiredMixin, UpdateViewMixin, UpdateView):
    model = Diagnostico
    template_name = 'core/diagnostic/form.html'
    form_class = DiagnosticoForm
    success_url = reverse_lazy('core:diagnostic_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Diagnóstico'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        diagnostic = self.object
        save_audit(self.request, diagnostic, action='M')
        messages.success(self.request, f"Éxito al modificar el diagnóstico {diagnostic.codigo} - {diagnostic.descripcion}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al modificar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

# Vista para eliminar un diagnóstico
class DiagnosticDeleteView(LoginRequiredMixin, DeleteViewMixin, DeleteView):
    model = Diagnostico
    success_url = reverse_lazy('core:diagnostic_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Diagnóstico'
        context['description'] = f"¿Desea eliminar lógicamente el diagnóstico: {self.object.codigo} - {self.object.descripcion}?"
        context['back_url'] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente el diagnóstico {self.object.codigo} - {self.object.descripcion}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)

# Vista para mostrar los detalles de un diagnóstico
class DiagnosticDetailView(LoginRequiredMixin, DetailView):
    model = Diagnostico

    def get(self, request, *args, **kwargs):
        diagnostic = self.get_object()
        data = {
            'id': diagnostic.id,
            'codigo': diagnostic.codigo,
            'descripcion': diagnostic.descripcion,
            'datos_adicionales': diagnostic.datos_adicionales,
            'activo': diagnostic.activo,
            # Añade más campos si es necesario
        }
        return JsonResponse(data)

