from django.urls import path

from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel, \
    SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDel, \
        MarcaView, MarcaNew, MarcaEdit, marca_inactivar, \
            UnidadMedidaView, UnidadMedidaNew, UnidadMedidaEdit, unidad_medida_inactivar

urlpatterns = [
    # Rutas de Categoria
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>', CategoriaDel.as_view(), name='categoria_del'),

    # Rutas de Subcategoria
    path('subcategoria/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategoria/new/', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategoria/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategoria/delete/<int:pk>', SubCategoriaDel.as_view(), name='subcategoria_del'),

    # Rutas de Marca
    path('marca/', MarcaView.as_view(), name='marca_list'),
    path('marca/new', MarcaNew.as_view(), name='marca_new'),
    path('marca/edit/<int:pk>', MarcaEdit.as_view(), name='marca_edit'),
    path('marca/inactivar/<int:id>', marca_inactivar, name='marca_inactivar'),

    # Rutas de Unidad de Medida
    path('um/', UnidadMedidaView.as_view(), name='um_list'),
    path('um/new', UnidadMedidaNew.as_view(), name='um_new'),
    path('um/edit/<int:pk>', UnidadMedidaEdit.as_view(), name='um_edit'),
    path('um/inactivar/<int:id>', unidad_medida_inactivar, name='um_inactivar'),
]
