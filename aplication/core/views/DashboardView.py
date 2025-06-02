from django.views.generic import TemplateView
from django.db.models import Count
from django.db.models.functions import TruncMonth
import json

class DashboardView(TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Simulación o consulta real de datos
        # Si tienes modelos para citas y atenciones:
        # from .models import Appointment, Attention
        # citas = Appointment.objects.annotate(mes=TruncMonth('date')).values('mes').annotate(cantidad=Count('id'))
        # atenciones = Attention.objects.annotate(mes=TruncMonth('date')).values('mes').annotate(cantidad=Count('id'))

        citas_data = {
            "labels": ["Enero", "Febrero", "Marzo"],
            "data": [10, 20, 15]
        }

        atenciones_data = {
            "labels": ["Juan Pérez", "Ana Gómez", "Carlos López"],
            "data": [5, 12, 8]
        }

        # Añadiendo datos serializados al contexto
        context['citas_data'] = json.dumps(citas_data)
        context['atenciones_data'] = json.dumps(atenciones_data)

        return context
