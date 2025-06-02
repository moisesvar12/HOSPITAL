from django import forms
from django.forms import ModelForm, ValidationError
from aplication.core.models import Diagnostico

class DiagnosticoForm(ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['codigo', 'descripcion', 'datos_adicionales', 'activo']
        
        widgets = {
            'descripcion': forms.Textarea(
                attrs={
                    "placeholder": "Descripción del diagnóstico",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            'datos_adicionales': forms.Textarea(
                attrs={
                    "placeholder": "Datos adicionales sobre el diagnóstico",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            'codigo': forms.TextInput(
                attrs={
                    "placeholder": "Código del diagnóstico",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            'activo': forms.CheckboxInput(
                attrs={
                    "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                }
            ),
        }

        labels = {
            "codigo": "Código del Diagnóstico",
            "descripcion": "Descripción del Diagnóstico",
            "datos_adicionales": "Datos Adicionales",
            "activo": "Activo",
        }

    # Validaciones personalizadas
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")
        if len(descripcion) < 10:
            raise ValidationError("La descripción debe contener al menos 10 caracteres.")
        return descripcion

    def clean_codigo(self):
        codigo = self.cleaned_data.get("codigo")
        if len(codigo) < 5:
            raise ValidationError("El código debe contener al menos 5 caracteres.")
        
        # Verificar si el código ya existe
        if Diagnostico.objects.filter(codigo=codigo).exists():
            raise ValidationError("Este código de diagnóstico ya existe.")
        
        return codigo
