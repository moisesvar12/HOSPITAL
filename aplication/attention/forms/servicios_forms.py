from django import forms
from aplication.attention.models import ServiciosAdicionales

class ServiciosAdicionalesForm(forms.ModelForm):
    class Meta:
        model = ServiciosAdicionales
        fields = ["nombre_servicio", "costo_servicio", "descripcion", "activo"]
        widgets = {
            "nombre_servicio": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese el nombre del servicio",
                    "class": "form-control"
                }
            ),
            "costo_servicio": forms.NumberInput(
                attrs={
                    "placeholder": "Ingrese el costo del servicio",
                    "class": "form-control",
                    "step": "0.01",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese una descripción opcional",
                    "class": "form-control",
                    "rows": 3,
                }
            ),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        labels = {
            "nombre_servicio": "Nombre del Servicio",
            "costo_servicio": "Costo del Servicio",
            "descripcion": "Descripción",
            "activo": "¿Está activo?",
        }
