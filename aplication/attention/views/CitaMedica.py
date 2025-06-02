from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from aplication.attention.models import CitaMedica


class CitaMedicaListView(ListView):
    model = CitaMedica
    template_name = 'core/CitaMedica/cita_list.html'
    context_object_name = 'citas'

class CitaMedicaDetailView(DetailView):
    model = CitaMedica
    template_name = 'core/CitaMedica/cita_detail.html'
    context_object_name = 'cita'

class CitaMedicaCreateView(CreateView):
    model = CitaMedica
    fields = ['paciente', 'fecha', 'hora_cita', 'estado']
    template_name = 'core/CitaMedica/cita_form.html'
    success_url = reverse_lazy('core:cita_list')

class CitaMedicaUpdateView(UpdateView):
    model = CitaMedica
    fields = ['paciente', 'fecha', 'hora_cita', 'estado']
    template_name = 'core/CitaMedica/cita_form.html'
    success_url = reverse_lazy('core:cita_list')


class CitaMedicaDeleteView(DeleteView):
    model = CitaMedica
    template_name = 'core/CitaMedica/cita_confirm_delete.html'
    success_url = reverse_lazy('core:cita_list')
