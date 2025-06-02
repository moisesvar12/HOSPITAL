from django.urls import reverse_lazy
from aplication.core.forms.empleado import EmpleadoForm
from aplication.core.models import Empleado
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class EmpleadoListView(ListView):
    template_name = "core/empleado/list.html"
    model = Empleado
    context_object_name = "empleados"
    query = None
    paginate_by = 2

    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get("q")  # ver
        sex = self.request.GET.get("sex")
        if q1 is not None:
            self.query.add(Q(nombres__icontains=q1), Q.OR)
            self.query.add(Q(apellidos__icontains=q1), Q.OR)
            self.query.add(Q(cedula__icontains=q1), Q.OR)
        if sex == "M" or sex == "F":
            self.query.add(Q(sexo__icontains=sex), Q.AND)
        return self.model.objects.filter(self.query).order_by("apellidos")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "SaludSync"
        context["title1"] = "Consulta de Empleado"
        return context


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "core/empleado/form.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy("core:empleado_list")
    # permission_required = 'add_supplier' # en PermissionMixn se verfica si un grupo tiene el permiso

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title"] = "SaludSync"
        context["title1"] = "Ingresar informacion del Empleado"
        context["grabar"] = "Grabar Empleado"
        context["back_url"] = self.success_url
        return context

    def form_valid(self, form):
        # print("entro al form_valid")
        response = super().form_valid(form)
        patient = self.object
        save_audit(self.request, patient, action="A")
        messages.success(
            self.request, f"Éxito al crear al empleado {patient.nombre_completo}."
        )
        return response

    def form_invalid(self, form):
        messages.error(
            self.request, "Error al enviar el formulario. Corrige los errores."
        )
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "core/empleado/form.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy("core:empleado_list")
    # permission_required = 'change_patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title"] = "SaludSync"
        context["title1"] = "Modificar informacion del empleadoe"
        context["grabar"] = "Actualizar empleadoe"
        context["back_url"] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        patient = self.object
        save_audit(self.request, patient, action="M")
        messages.success(
            self.request, f"Éxito al Modificar el empleadoe {patient.nombre_completo}."
        )
        print("mande mensaje")
        return response

    def form_invalid(self, form):
        messages.error(
            self.request, "Error al Modificar el formulario. Corrige los errores."
        )
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    # template_name = 'core/patient/form.html'
    success_url = reverse_lazy("core:empleado_list")
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title"] = "SaludSync"
        context["grabar"] = "Eliminar Al empleadoe"
        context["description"] = f"¿Desea Eliminar al empleadoe: {self.object.name}?"
        context["back_url"] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = (
            f"Éxito al eliminar lógicamente al empleado {self.object.name}."
        )
        messages.success(self.request, success_message)
        # Cambiar el estado de eliminado lógico
        # self.object.deleted = True
        # self.object.save()
        return super().delete(request, *args, **kwargs)


class EmpleadoDetailView(DetailView):
    model = Empleado

    def get(self, request, *args, **kwargs):
        empleado = self.get_object()
        data = {
            "id": empleado.id,
            "nombres": empleado.nombres,
            "apellidos": empleado.apellidos,
            "foto": empleado.get_image(),
            "fecha_nac": empleado.fecha_nacimiento,
            "dni": empleado.cedula,
            "direccion": empleado.direccion,
            # Añade más campos según tu modelo
        }
        return JsonResponse(data)
