from django.forms import ModelForm, ValidationError
from django import forms
from aplication.core.models import Especialidad 

class EspecialidadForm(ModelForm):
    class Meta:
        model = Especialidad
        fields = [
            "nombre", "descripcion", "activo"
        ]
        error_messages = {
            "nombre": {
                "unique": "Ya existe una especialidad con este nombre.",
            },
        }
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese el nombre de la especialidad",
                    "id": "id_nombre",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese una descripción de la especialidad",
                    "id": "id_descripcion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                    "rows": 4,
                }
            ),
            "activo": forms.CheckboxInput(
                attrs={
                    "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                }
            ),
        }
        labels = {
            "nombre": "Nombre de la Especialidad",
            "descripcion": "Descripción",
            "activo": "Activo",
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if not nombre or len(nombre) < 2:
            raise ValidationError("El nombre debe tener al menos 2 caracteres.")
        return nombre.upper()

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")
        if not descripcion or len(descripcion) < 5:
            raise ValidationError("La descripción debe tener al menos 5 caracteres.")
        return descripcion.capitalize()
