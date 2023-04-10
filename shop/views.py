from django.shortcuts import render, get_object_or_404
from .models import Product
from cart.cart import Cart
from main_page.views import menu

products = Product.objects.filter(available=True)

def shop_view(request):
    cart = Cart(request)
    return render(request, 'shop.html', context={'menu': menu,
                                                 'num_el': 2,
                                                 'products': products,
                                                 'cart': cart})


def product_detail(request, id, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop-single.html', {'menu': menu,
                                                'num_el': 2,
                                                'products': products,
                                                'product': product,
                                                'cart': cart, })

def cart_view(request):

    cart = Cart(request)
    return render(request, 'cart.html', context={'menu': menu,
                                                 'num_el': 2,
                                                 'products': products,
                                                 'cart': cart, })


# def product_list(request, category_slug=None):
#     cart = Cart(request)
#     products = Product.objects.filter(available=True)
#     return render(request, 'list.html', {'products': products, 'cart': cart})
