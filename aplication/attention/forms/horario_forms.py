from django.forms import ModelForm, ValidationError
from django import forms
from aplication.attention.models import HorarioAtencion

from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from aplication.attention.models import HorarioAtencion

class HorarioAtencionForm(ModelForm):
    class Meta:
        model = HorarioAtencion
        fields = ["dia_semana", "hora_inicio", "hora_fin", "Intervalo_desde", "Intervalo_hasta", "activo"]
        widgets = {
            "dia_semana": forms.Select(
                attrs={
                    "id": "id_dia_semana",
                    "class": (
                        "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 "
                        "rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full "
                        "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 "
                        "dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
                    ),
                }
            ),
            "hora_inicio": forms.TimeInput(
                format='%H:%M',
                attrs={
                    "type": "time",
                    "placeholder": "Ingrese hora de inicio",
                    "id": "id_hora_inicio",
                    "class": (
                        "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 "
                        "rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full "
                        "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 "
                        "dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
                    ),
                }
            ),
            "hora_fin": forms.TimeInput(
                format='%H:%M',
                attrs={
                    "type": "time",
                    "placeholder": "Ingrese hora de fin",
                    "id": "id_hora_fin",
                    "class": (
                        "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 "
                        "rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full "
                        "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 "
                        "dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
                    ),
                }
            ),
            "Intervalo_desde": forms.TimeInput(
                format='%H:%M',
                attrs={
                    "type": "time",
                    "placeholder": "Ingrese hora de inicio del intervalo",
                    "id": "id_intervalo_desde",
                    "class": (
                        "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 "
                        "rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full "
                        "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 "
                        "dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
                    ),
                }
            ),
            "Intervalo_hasta": forms.TimeInput(
                format='%H:%M',
                attrs={
                    "type": "time",
                    "placeholder": "Ingrese hora de fin del intervalo",
                    "id": "id_intervalo_hasta",
                    "class": (
                        "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 "
                        "rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full "
                        "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 "
                        "dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
                    ),
                }
            ),
            "activo": forms.CheckboxInput(
                attrs={
                    "id": "id_activo",
                    "class": (
                        "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm "
                        "focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    ),
                }
            ),
        }
        labels = {
            "dia_semana": "Día de la Semana",
            "hora_inicio": "Hora de Inicio",
            "hora_fin": "Hora de Fin",
            "Intervalo_desde": "Intervalo Desde",
            "Intervalo_hasta": "Intervalo Hasta",
            "activo": "¿Activo?",
        }

    def clean(self):
        """Validación adicional para coherencia de horarios."""
        cleaned_data = super().clean()
        hora_inicio = cleaned_data.get("hora_inicio")
        hora_fin = cleaned_data.get("hora_fin")
        intervalo_desde = cleaned_data.get("Intervalo_desde")
        intervalo_hasta = cleaned_data.get("Intervalo_hasta")

        if hora_inicio and hora_fin:
            if hora_inicio >= hora_fin:
                raise ValidationError("La hora de inicio debe ser menor que la hora de fin.")
        
        if intervalo_desde and intervalo_hasta:
            if intervalo_desde >= intervalo_hasta:
                raise ValidationError("El intervalo de descanso debe tener un inicio antes que el fin.")
            if not (hora_inicio <= intervalo_desde < hora_fin):
                raise ValidationError("El intervalo de descanso debe comenzar dentro del horario de atención.")
            if not (hora_inicio < intervalo_hasta <= hora_fin):
                raise ValidationError("El intervalo de descanso debe terminar dentro del horario de atención.")

        return cleaned_data
