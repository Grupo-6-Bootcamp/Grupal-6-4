from django import forms
from .models import Proveedores


class FormularioProveedores(forms.ModelForm):

    class Meta:
        model = Proveedores
        fields = ('nombre', 'rut', 'direccion', 'telefono', 'email')
        labels = {
            'nombre': 'Nombre',
            'rut': 'Rut',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'email': 'Email'
        }
