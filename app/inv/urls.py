from django.urls import path

from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel, \
    SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDel

urlpatterns = [
    # Rutas de Categoria
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>', CategoriaDel.as_view(), name='categoria_del'),

    # Rutas de Subcategoria
    path('subcategoria/', SubCategoriaView.as_view(),name='subcategoria_list'),
    path('subcategoria/new/', SubCategoriaNew.as_view(),name='subcategoria_new'),
    path('subcategoria/edit/<int:pk>', SubCategoriaEdit.as_view(),name='subcategoria_edit'),
    path('subcategoria/delete/<int:pk>', SubCategoriaDel.as_view(),name='subcategoria_del'),
]
