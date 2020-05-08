# Clases
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

# Decoradores
from django.contrib.auth.decorators import login_required, permission_required

# Modelos
from .models import Categoria, Subcategoria, Marca,\
    UnidadMedida, Producto
# Formularios
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm,\
    UnidadMedidaForm, ProductoForm
# Vistas de otra app
from bases.views import Sinprivilegios


# Categoria.
class CategoriaView(Sinprivilegios, generic.ListView):
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"


class CategoriaNew(Sinprivilegios, generic.CreateView):
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    success_message = "Categoria creada correctamente"

    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user
        return super().form_valid(form)


class CategoriaEdit(Sinprivilegios, generic.UpdateView):
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    success_message = "Categoria actualizada correctamente"

    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id 
        return super().form_valid(form)


class CategoriaDel(Sinprivilegios, generic.DeleteView):
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy('inv:categoria_list')

# Sub categoria
class SubCategoriaView(Sinprivilegios, generic.ListView):
    permission_required = "inv.view_subcategoria"
    model = Subcategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"


class SubCategoriaNew(Sinprivilegios, generic.CreateView):
    permission_required = "inv.view_subcategoria"
    model = Subcategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    success_message = "Subcategoria creada correctamente"

    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user
        return super().form_valid(form)


class SubCategoriaEdit(Sinprivilegios, generic.UpdateView):
    permission_required = "inv.view_subcategoria"
    model = Subcategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    success_message = "Subcategoria actualizada correctamente"

    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id 
        return super().form_valid(form)


class SubCategoriaDel(Sinprivilegios, generic.DeleteView):
    permission_required = "inv.view_subcategoria"
    model = Subcategoria
    template_name = "inv/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy('inv:subcategoria_list')
    success_message = "Subcategoria eliminada correctamente"


#Marca
class MarcaView(Sinprivilegios, generic.ListView):
    permission_required = "inv.view_marca"
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"


class MarcaNew(Sinprivilegios, generic.CreateView):
    permission_required = "inv.view_marca"
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    success_url = reverse_lazy('inv:marca_list')
    success_message = "Marca creada correctamente"
    form_class = MarcaForm

    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user
        return super().form_valid(form)


class MarcaEdit(Sinprivilegios, generic.UpdateView):
    permission_required = "inv.view_marca"
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    success_url = reverse_lazy('inv:marca_list')
    success_message = "Marca creada correctamente"
    form_class = MarcaForm


    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user
        return super().form_valid(form)


@login_required(login_url='/login/')
@permission_required('inv.change_marca', login_url='bases:sin_privilegios')
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not marca:
        return redirect('inv:marca_list')

    if request.method == 'GET':
        contexto = {'obj':marca}

    if request.method == 'POST':
        marca.estado = False
        marca.save()
        messages.error(request, 'Marca Inactivada.')
        return redirect('inv:marca_list')

    return render(request, template_name, contexto)


#Unida de medida
class UnidadMedidaView(Sinprivilegios, generic.ListView):
    permission_required = "inv.view_unidadmedida"
    model = UnidadMedida
    template_name= "inv/um_list.html"
    context_object_name = "obj"


class UnidadMedidaNew(Sinprivilegios, generic.CreateView):
    permission_required = "inv.view_unidadmedida"
    model = UnidadMedida
    template_name = "inv/um_form.html"
    context_object_name = "obj"
    success_url = reverse_lazy('inv:um_list')
    success_message = "Unidad de medida creada correctamente"
    form_class = UnidadMedidaForm

    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user
        return super().form_valid(form)
    

class UnidadMedidaEdit(Sinprivilegios, generic.UpdateView):
    permission_required = "inv.view_unidadmedida"
    model = UnidadMedida
    template_name = "inv/um_form.html"
    context_object_name = "obj"
    success_url = reverse_lazy('inv:um_list')
    success_message = "Unidad de medida editada correctamente"
    form_class = UnidadMedidaForm

    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user
        return super().form_valid(form)


@login_required(login_url='/login/')
@permission_required('inv.change_unidadmedida', login_url='bases:sin_privilegios')
def unidad_medida_inactivar(request, id):
    unidad_medida = UnidadMedida.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not unidad_medida:
        return redirect('inv:um_list')

    if request.method == 'GET':
        contexto = {'obj':unidad_medida}

    if request.method == 'POST':
        unidad_medida.estado = False
        unidad_medida.save()
        return redirect('inv:um_list')

    return render(request, template_name, contexto)


class ProductoView(Sinprivilegios, generic.ListView):
    permission_required = "inv.view_producto"
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"


class ProductoNew(Sinprivilegios, generic.CreateView):
    permission_required = "inv.view_producto"
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    success_url = reverse_lazy('inv:producto_list')
    success_message = "Producto creado correctamente"
    form_class = ProductoForm
    
    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user
        return super().form_valid(form)


class ProductoEdit(Sinprivilegios, generic.UpdateView):
    permission_required = "inv.view_producto"
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    success_url = reverse_lazy('inv:producto_list')
    success_message = "Producto editado correctamente"
    form_class = ProductoForm

    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user 
        return super().form_valid(form)


@login_required(login_url='/login/')
@permission_required('inv.change_producto', login_url='bases:sin_privilegios')
def producto_inactivar(request, id):
    producto = Producto.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not producto:
        return redirect('inv:producto_list')

    if request.method == 'GET':
        contexto = {'obj':producto}

    if request.method == 'POST':
        producto.estado = False
        producto.save()
        return redirect('inv:producto_list')

    return render(request, template_name, contexto)