from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from aplication.core.models import Certificado
from aplication.attention.forms.certificate import CertificadoForm
from doctor.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, UpdateViewMixin
from doctor.utils import save_audit

class CertificateCreateView(CreateViewMixin, CreateView):
    model = Certificado
    template_name= 'core/certificado/form.html'
    form_class = CertificadoForm
    success_url = reverse_lazy('attention:certificate_list')

class CertificateListView(ListViewMixin, ListView):
    model = Certificado
    template_name = 'core/certificado/list.html'
    context_object_name = 'certificados'

    def get_queryset(self):
        paciente_id = self.request.GET.get('paciente_id')
        query = Q()
        if paciente_id:
            query.add(Q(paciente__id=paciente_id), Q.AND)
        return self.model.objects.filter(query).order_by('-fecha_emision')

class CertificateUpdateView(UpdateViewMixin, UpdateView):
    template_name= 'core/certificado/form.html'
    model = Certificado
    form_class = CertificadoForm
    success_url = reverse_lazy('core:certificate_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'GET':
            context['grabar'] = 'Grabar Certificado'
        else:
            context['grabar'] = 'Actualizar Certificado'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        certificado = self.object
        if self.request.method == 'POST':
            save_audit(self.request, certificado, action='A')
            messages.success(self.request, f"Éxito al crear el certificado para {certificado.paciente.nombre_completo}.")
        else:
            save_audit(self.request, certificado, action='M')
            messages.success(self.request, f"Éxito al modificar el certificado para {certificado.paciente.nombre_completo}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar/modificar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

class CertificateDeleteView(DeleteViewMixin, DeleteView):
    model = Certificado
    success_url = reverse_lazy('core:certificate_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(self.request, f"Certificado de {self.object.paciente.nombre_completo} eliminado con éxito.")
        return super().delete(request, *args, **kwargs)

class CertificateDetailView(DetailView):
    model = Certificado

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            certificado = self.get_object()
            data = {
                'id': certificado.id,
                'paciente': certificado.paciente.nombre_completo,
                'diagnostico': certificado.diagnostico,
                'tratamiento': certificado.tratamiento,
                'observaciones': certificado.observaciones,
                'fecha_emision': certificado.fecha_emision,
                'medico_responsable': certificado.medico_responsable
            }
            return JsonResponse(data)
        else:
            return super().get(request, *args, **kwargs)
