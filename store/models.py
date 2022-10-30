from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200,unique=True,verbose_name="Nombre del producto")
    slug = models.SlugField(max_length=200,unique=True,verbose_name="Enlace")
    description = models.TextField(max_length=500,blank=True,verbose_name="Descripción")
    price = models.IntegerField(verbose_name="Precio")
    images = models.ImageField(upload_to='photos/products',verbose_name="Imagen")
    stock = models.IntegerField(verbose_name="Existencias")
    is_available = models.BooleanField(default=True,verbose_name="Disponible")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Categoria")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    modified_date = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def get_url(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.product_name


