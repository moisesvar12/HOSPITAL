from django import forms
from aplication.core.models import ExamenMedico

class ExamenForm(forms.ModelForm):
    class Meta:
        model = ExamenMedico
        fields = ['paciente', 'fecha_examen', 'resultado', 'diagnostico', 'medicamentos_recomendados', 
                  'comentarios', 'tipo_examen', 'observaciones', 'activo']

        widgets = {
            'fecha_examen': forms.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "Ingrese la fecha del examen",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            'resultado': forms.Textarea(
                attrs={
                    "placeholder": "Ingrese el resultado del examen",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            'diagnostico': forms.Textarea(
                attrs={
                    "placeholder": "Ingrese el diagnóstico relacionado al examen",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            'medicamentos_recomendados': forms.Textarea(
                attrs={
                    "placeholder": "Ingrese los medicamentos recomendados",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            'comentarios': forms.Textarea(
                attrs={
                    "placeholder": "Comentarios adicionales",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            'tipo_examen': forms.TextInput(
                attrs={
                    "placeholder": "Tipo de examen",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            'observaciones': forms.Textarea(
                attrs={
                    "placeholder": "Observaciones adicionales",
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
            'paciente': 'Paciente',
            'fecha_examen': 'Fecha del Examen',
            'resultado': 'Resultado',
            'diagnostico': 'Diagnóstico',
            'medicamentos_recomendados': 'Medicamentos Recomendados',
            'comentarios': 'Comentarios',
            'tipo_examen': 'Tipo de Examen',
            'observaciones': 'Observaciones',
            'activo': 'Activo',
        }

    # Validaciones personalizadas
    def clean_resultado(self):
        resultado = self.cleaned_data.get('resultado')
        if len(resultado) < 10:
            raise forms.ValidationError('El resultado del examen debe contener al menos 10 caracteres.')
        return resultado

    def clean_diagnostico(self):
        diagnostico = self.cleaned_data.get('diagnostico')
        if len(diagnostico) < 10:
            raise forms.ValidationError('El diagnóstico debe contener al menos 10 caracteres.')
        return diagnostico