from django import forms

from .models import Categoria, Subcategoria, Marca, UnidadMedida, Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion','estado']
        labels = {'descripcion':"Descripcion de la Categoria",
        'estado':"Estado"}
        widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args ,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':"form-control"
            })


class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset= Categoria.objects.filter(estado=True)
        .order_by('descripcion')
    )
    class Meta:
        model = Subcategoria
        fields = ['categoria','descripcion','estado']
        labels = {'descripcion':"Sub categoria",
        'estado':"Estado"}
        widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args ,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':"form-control"
            })
        self.fields['categoria'].empty_label = "Seleccione Categoria"


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['descripcion','estado']
        labels = {'descripcion':"Descripción",
        'estado':"Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args ,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':"form-control"
            })


class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ['descripcion','estado']
        labels = {'descripcion':"Descripcion",
        'estado':"Estado"}
        widget = {'descripcion': forms.TextInput}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args ,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':"form-control"
            })


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo','codigo_barra','descripcion','estado',
                  'precio','existencia','ultima_compra',
                  'marca','subcategoria','unidad_medida']
        exclude = ['usuario_modifica','fecha_modificacion','usuario_creador','fecha_creacion']
        widget = {'descripcion':forms.TextInput()}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args ,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':"form-control"
            })
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True