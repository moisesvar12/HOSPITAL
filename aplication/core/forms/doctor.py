from django.forms import ModelForm, ValidationError
from django import forms
from aplication.core.models import Doctor

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = [
            "nombres", "apellidos", "cedula", "especialidad", 
            "latitud", "longitud", "horario_atencion", "curriculum",
            "firmaDigital", "imagen_receta", "telefonos", "email", 
            "direccion", "activo", "fecha_nacimiento", "codigoUnicoDoctor", 
            "foto"
        ]
        error_messages = {
            "email": {
                "unique": "Ya existe un doctor registrado con este email.",
            },
        }
        widgets = {
            "nombres": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombres",
                    "id": "id_nombres",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 rounded-lg focus:ring-blue-500 block w-full p-2.5",
                }
            ),
            "apellidos": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese apellidos",
                    "id": "id_apellidos",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 rounded-lg focus:ring-blue-500 block w-full p-2.5",
                }
            ),
            "cedula": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese cédula",
                    "id": "id_cedula",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 rounded-lg focus:ring-blue-500 block w-full p-2.5",
                }
            ),
            "codigoUnicoDoctor": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese código único del doctor",
                    "id": "id_codigoUnicoDoctor",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 rounded-lg focus:ring-blue-500 block w-full p-2.5",
                }
            ),
            "especialidad": forms.CheckboxSelectMultiple(
                attrs={
                    "id": "id_especialidad",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full",
                }
            ),
            "fecha_nacimiento": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 rounded-lg block w-full p-2.5",
                }
            ),
            "telefonos": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese teléfono o celular",
                    "id": "id_telefonos",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 rounded-lg block w-full p-2.5",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Ingrese correo electrónico",
                    "id": "id_email",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 rounded-lg block w-full p-2.5",
                }
            ),
            "direccion": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese dirección",
                    "id": "id_direccion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 rounded-lg block w-full p-2.5",
                }
            ),
            "latitud": forms.NumberInput(
                attrs={
                    "placeholder": "Ingrese latitud",
                    "id": "id_latitud",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 rounded-lg block w-full p-2.5",
                }
            ),
            "longitud": forms.NumberInput(
                attrs={
                    "placeholder": "Ingrese longitud",
                    "id": "id_longitud",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 rounded-lg block w-full p-2.5",
                }
            ),
            "horario_atencion": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese horario de atención",
                    "id": "id_horario_atencion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 rounded-lg block w-full p-2.5",
                }
            ),
            "curriculum": forms.FileInput(
                attrs={
                    "id": "id_curriculum",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 rounded-lg block w-full p-2.5",
                }
            ),
            "firmaDigital": forms.FileInput(
                attrs={
                    "id": "id_firmaDigital",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 rounded-lg block w-full p-2.5",
                }
            ),
            "imagen_receta": forms.FileInput(
                attrs={
                    "id": "id_imagen_receta",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 rounded-lg block w-full p-2.5",
                }
            ),
            "foto": forms.FileInput(
                attrs={
                    "id": "id_foto",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 rounded-lg block w-full p-2.5",
                }
            ),
            "activo": forms.CheckboxInput(
                attrs={
                    "id": "id_activo",
                    "class": "form-check-input",
                }
            ),
        }
        labels = {
            "cedula": "DNI",
            "curriculum": "Curriculum Vitae",
            "firmaDigital": "Firma Digital",
            "imagen_receta": "Imagen de Receta",
            "foto": "Foto del Doctor",
        }

    # Validaciones personalizadas
    def clean_nombres(self):
        nombres = self.cleaned_data.get("nombres")
        if not nombres or len(nombres) < 2:
            raise ValidationError("El nombre debe tener al menos 2 caracteres.")
        return nombres.upper()

    def clean_apellidos(self):
        apellidos = self.cleaned_data.get("apellidos")
        if not apellidos or len(apellidos) < 1:
            raise ValidationError("El apellido debe tener al menos 1 carácter.")
        return apellidos.upper()
