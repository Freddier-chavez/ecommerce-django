from django.db import models
from store.models import Product, Variation
# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250,blank=True,verbose_name="Código carrito")
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
    class Meta:
        verbose_name = 'carrito'
        verbose_name_plural = 'carritos'


class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="Producto")
    variations = models.ManyToManyField(Variation,blank=True,verbose_name="Variaciones")
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,verbose_name="Código Carrito")
    quantity = models.IntegerField(verbose_name="Cantidad")
    is_active = models.BooleanField(default=True,verbose_name="Es activo")

    class Meta:
        verbose_name = 'artículo del carro'
        verbose_name_plural = 'artículos del carrito'

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product

    