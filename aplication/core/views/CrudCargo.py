from aplication.core.models import Cargo
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView,DetailView

class CargoListView(ListView):
    model = Cargo
    template_name= 'core/Cargo/list2.html'
    context_object_name='cargo1'


class CargoDetailView(DetailView):
    model= Cargo
    template_name = 'core/Cargo/detalle2.html'
    context_object_name='cargo'

class CargoCreateView(CreateView):
    model = Cargo
    fields = ['nombre','descripcion','activo']
    template_name = 'core/Cargo/form2.html'
    context_object_name='cargo'
    success_url = reverse_lazy('core:listarcargo')

class CargoUpdateView(UpdateView):
    model = Cargo
    fields = ['nombre','descripcion','activo']
    success_url = reverse_lazy('core:listarcargo')
    template_name = 'core/Cargo/editar2.html'
    context_object_name='cargo'


class CargoDeleteView(DeleteView):
    model = Cargo
    success_url = reverse_lazy('core:listarcargo')
    template_name = 'core/Cargo/eliminar2.html'
    context_object_name='cargo'