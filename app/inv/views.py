from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Categoria, Subcategoria
from .forms import CategoriaForm, SubCategoriaForm


# Categoria.
class CategoriaView(LoginRequiredMixin,generic.ListView):
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'


class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases.login'

    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user
        return super().form_valid(form)


class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases.login'

    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id 
        return super().form_valid(form)


class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = "inv/catalogos_del.html"
    context_object_name='obj'
    success_url = reverse_lazy('inv:categoria_list')

# Sub categoria
class SubCategoriaView(LoginRequiredMixin,generic.ListView):
    model = Subcategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'


class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = Subcategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'bases.login'

    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user
        return super().form_valid(form)


class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Subcategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'bases.login'

    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id 
        return super().form_valid(form)



class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Subcategoria
    template_name = "inv/catalogos_del.html"
    context_object_name='obj'
    success_url = reverse_lazy('inv:subcategoria_list')