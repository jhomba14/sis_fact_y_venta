from django.db import models

from bases.models import ClaseModelo

# Create your models here.
class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=250,
        help_text='Descripcion de la categoria',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()
    
    class Meta:
        verbose_name_plural = "Categorias"


class Subcategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=250,
        help_text='Descripcion de la categoria'
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Subcategoria, self).save()
    
    class Meta:
        verbose_name_plural = "Sub Categorias"
        unique_together = ('categoria', 'descripcion')


class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la marca',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()
    
    class Meta:
        verbose_name_plural = "Marca"



class UnidadMedida(ClaseModelo):
    descripcion = models.CharField(
        max_length = 100,
        help_text = 'Descripcion de la unidad de medida',
        unique = True 
    )

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()
    
    class Meta:
        verbose_name_plural = "Unidades de Medida"
    
    
class Producto(ClaseModelo):
    codigo = models.CharField(max_length=20, unique=True)
    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateTimeField(blank=True, null=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)

    def __str__(self):
        return '{}:{}:{}:{}:{}:{}:{}:{}:{}'.format(
            self.codigo,
            self.codigo_barra,
            self.descripcion,
            self.precio,
            self.existencia,
            self.ultima_compra,
            self.marca,
            self.unidad_medida,
            self.subcategoria
        )
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()
    
    class Meta:
        verbose_name_plural = "Productos"
        unique_together = ('codigo','codigo_barra')
    
