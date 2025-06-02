from django import forms
from django.forms import ModelForm, ValidationError
from aplication.core.models import Certificado, Paciente

class CertificadoForm(ModelForm):
    class Meta:
        model = Certificado
        # Campos que se incluyen en el formulario
        fields = [
            "paciente",
            "diagnostico",
            "tratamiento",
            "observaciones",
            "fecha_emision",
            "medico_responsable",
        ]
        # Personalización de widgets
        widgets = {
            "paciente": forms.Select(
                attrs={
                    "id": "id_paciente",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "diagnostico": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese el diagnóstico",
                    "id": "id_diagnostico",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "tratamiento": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese el tratamiento",
                    "id": "id_tratamiento",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "observaciones": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese observaciones (opcional)",
                    "id": "id_observaciones",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "fecha_emision": forms.DateInput(
                attrs={
                    "type": "date",
                    "id": "id_fecha_emision",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "medico_responsable": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese el nombre del médico responsable",
                    "id": "id_medico_responsable",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
        }

    # Validación personalizada del campo "diagnostico"
    def clean_diagnostico(self):
        diagnostico = self.cleaned_data.get("diagnostico")
        if not diagnostico or len(diagnostico) < 5:
            raise ValidationError("El diagnóstico debe tener al menos 5 caracteres.")
        return diagnostico

    # Validación personalizada del campo "tratamiento"
    def clean_tratamiento(self):
        tratamiento = self.cleaned_data.get("tratamiento")
        if not tratamiento or len(tratamiento) < 5:
            raise ValidationError("El tratamiento debe tener al menos 5 caracteres.")
        return tratamiento

    # Validación personalizada para asegurar que el médico responsable tenga al menos un nombre y un apellido
    def clean_medico_responsable(self):
        medico_responsable = self.cleaned_data.get("medico_responsable")
        if not medico_responsable or " " not in medico_responsable.strip():
            raise ValidationError("Ingrese el nombre completo del médico responsable (nombre y apellido).")
        return medico_responsable.title()

