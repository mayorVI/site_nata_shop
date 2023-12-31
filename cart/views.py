from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET

from shop.models import Product
from main_page.views import menu
from .cart import Cart

# Create your views here.


@require_GET
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1, update_quantity=False)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def unit_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove_one(product)
    return redirect('cart:cart_detail')



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart, 'menu': menu})
