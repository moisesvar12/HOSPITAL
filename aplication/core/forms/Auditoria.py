# forms.py
from django import forms
from aplication.core.models import Auditoria
from django.utils import timezone

class AuditoriaSearchForm(forms.Form):
    usuario = forms.CharField(required=False, label='Usuario')
    accion = forms.ChoiceField(
        choices=[('', 'Seleccione una acción'), ('A', 'Añadir'), ('M', 'Modificar'), ('E', 'Eliminar')],
        required=False, 
        label='Acción'
    )
    fecha_inicio = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date'}), 
        label="Desde"
    )
    fecha_fin = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date'}), 
        label="Hasta"
    )

    def filter_queryset(self, queryset):
        # Filtro por usuario
        usuario = self.cleaned_data.get('usuario')
        if usuario:
            queryset = queryset.filter(usuario__username__icontains=usuario)
        
        # Filtro por acción
        accion = self.cleaned_data.get('accion')
        if accion:
            queryset = queryset.filter(accion=accion)
        
        # Filtro por fechas
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        if fecha_inicio:
            queryset = queryset.filter(fecha__gte=fecha_inicio)
        
        fecha_fin = self.cleaned_data.get('fecha_fin')
        if fecha_fin:
            queryset = queryset.filter(fecha__lte=fecha_fin)
        
        return queryset
