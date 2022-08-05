from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Category, Product, Cart
from .form import CartAddForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def catalog(request):
    categories = Category.objects.all()
    return render(request, 'catalog.html', {'categories': categories}) 

def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category_id=category_id)
    return render(request,'category.html', {'category': category, 'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_product_form = CartAddForm()
    return render(request,'product.html', {'product': product, 'cart_product_form': cart_product_form})

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add_to_cart(product=product, quantity = cd['quantity'], update_quantity = cd['update'])
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove_from_cart(product)
    return redirect('cart_detail')
