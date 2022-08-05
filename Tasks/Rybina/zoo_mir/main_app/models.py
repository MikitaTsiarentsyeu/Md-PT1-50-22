from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.urls import reverse
from django.db import models
from decimal import Decimal
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='uploads')
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add_to_cart(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.cart_save()

    def cart_save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    
    def remove_from_cart(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.cart_save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for x in self.cart.values():
            x['price'] = Decimal(x['price'])
            x['total_price'] = x['price']*x['quantity']
            yield x

    def __len__(self):
        return sum(x['quantity'] for x in self.cart.values())

    def total_sum(self):
        return sum(Decimal(x['price'])*x['quantity'] for x in self.cart.values()) 

    def cart_clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True