from django.db import models

from . import managers


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='nombre')

    is_active = models.BooleanField(verbose_name='activo')

    objects = managers.CategoryManager.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'


class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name='name')

    category = models.ForeignKey('app.Category', on_delete=models.CASCADE, verbose_name='categoría')

    is_active = models.BooleanField(verbose_name='activo')

    objects = managers.ProductManager.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = 'producto'
        verbose_name_plural = 'productos'


class Restaurant(models.Model):
    name = models.CharField(max_length=64, verbose_name='name')

    is_active = models.BooleanField(verbose_name='activo')

    products = models.ManyToManyField('app.Product', blank=True, verbose_name='productos')

    objects = managers.RestaurantManager.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = 'restaurante'
        verbose_name_plural = 'restaurantes'
