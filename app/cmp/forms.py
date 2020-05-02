from django import forms

from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)
    class Meta:
        model = Proveedor
        exclude = ['usuario_modifica','fecha_modificacion','usuario_creador','fecha_creacion']
        widget={'descripcion': forms.TextInput()}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args ,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':"form-control"
            })


    
