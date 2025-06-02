from django.forms import ModelForm, ValidationError
from django import forms
from aplication.core.models import TipoSangre  # Importa tu modelo de tipo de sangre

class TipoSangreForm(ModelForm):
    class Meta:
        model = TipoSangre
        fields = ["descripcion", "tipo"]
        
        # Mensajes de error personalizados
        error_messages = {
            "descripcion": {
                "unique": "Este tipo de sangre ya está registrado.",
            },
        }
        
        # Personalización de los widgets en el formulario HTML
        widgets = {
            "descripcion": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese tipo de sangre (Ej: A+, O-)",
                    "id": "id_descripcion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
        }
        
        # Etiquetas personalizadas para los campos
        labels = {
            "descripcion": "Tipo de Sangre",
            "tipo": "Tipo",
        }

    # Método de limpieza para el campo 'descripcion'
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")
        if not descripcion or len(descripcion) < 2:
            raise ValidationError("La descripción del tipo de sangre debe tener al menos 2 caracteres.")
        return descripcion.upper()
