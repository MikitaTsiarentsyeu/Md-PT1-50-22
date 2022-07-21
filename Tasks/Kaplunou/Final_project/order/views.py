from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from order.forms import AddQuantityForm
from order.models import Order, OrderItem, Product 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



#def get_gear(request):
#    response = render_to_string('order/store_page.html')
#    return HttpResponse(response)
    

def index(request):    
    return render(request, 'order/start_page.html')

def about(request):   
    return render(request, 'order/about.html')

def contacts(request):
    return render(request, 'order/contacts.html')


class ProductsListView(ListView):
    model = Product
    template_name = 'order/store_page.html'

class ProductsDetailView(DetailView):
    model = Product
    template_name = 'order/details.html'

@login_required(login_url=reverse_lazy('login'))
def add_item_to_cart(request, pk):
    if request.method == 'POST':
        quantity_form = AddQuantityForm(request.POST)
        if quantity_form.is_valid():
            quantity = quantity_form.cleaned_data['quantity']
            if quantity:
                cart = Order.get_cart(request.user)
                product = get_object_or_404(Product, pk=pk)
                cart.orderitem_set.create(product=product,
                                          quantity=quantity,
                                          price=product.price)
                cart.save()
                return redirect('cart')
        else:
            pass
    return redirect('shop')

@login_required(login_url=reverse_lazy('login'))
def cart_view(request):
    cart = Order.get_cart(request.user)
    items = cart.orderitem_set.all()
    context = {
        'cart': cart,
        'items': items,
    }
    return render(request, 'order/cart.html', context)

@method_decorator(login_required, name='dispatch')
class CartDeleteItem(DeleteView):
    model = OrderItem
    template_name = 'cart.html'
    success_url = reverse_lazy('cart')

    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(order__user=self.request.user)
        return qs

@login_required(login_url=reverse_lazy('login'))
def make_order(request):
    cart = Order.get_cart(request.user)
    cart.make_order()
    return redirect('shop')