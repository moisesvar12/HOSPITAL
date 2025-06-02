from django import forms

class FaceRegisterForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ingresa tu nombre de usuario'
        }),
        label="Nombre de Usuario"
    )
    face_data = forms.CharField(
        required=True,
        widget=forms.HiddenInput(),
        label="Datos Faciales"
    )
