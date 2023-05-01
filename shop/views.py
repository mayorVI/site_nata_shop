from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Product
from cart.cart import Cart
from main_page.views import menu, lines, brands, categories

products = Product.objects.filter(available=True)


def shop_view(request):
    cart = Cart(request)
    return render(request, 'shop.html', context={'menu': menu,
                                                 'num_el': 2,
                                                 'brands': brands,
                                                 'categories': categories,
                                                 'lines': lines,
                                                 'products': products,
                                                 'cart': cart})

def brands_view(request):
    cart = Cart(request)
    return render(request, 'brand.html', context={'menu': menu,
                                                  'num_el': 2,
                                                  'brands': brands,
                                                  'categories': categories,
                                                  'lines': lines,
                                                  'products': products,
                                                  'cart': cart})
def lines_view(request):
    cart = Cart(request)
    return render(request, 'lines.html', context={'menu': menu,
                                                  'num_el': 4,
                                                  'brands': brands,
                                                  'categories': categories,
                                                  'lines': lines,
                                                  'products': products,
                                                  'cart': cart})

def cats_view(request):
    cart = Cart(request)
    return render(request, 'categories.html', context={'menu': menu,
                                                  'num_el': 3,
                                                  'brands': brands,
                                                  'categories': categories,
                                                  'lines': lines,
                                                  'products': products,
                                                  'cart': cart})

def brand_view(request,  id):
    cart = Cart(request)
    brand = get_object_or_404(Product, id=id, available=True)
    if id == 4:
        products = Product.objects.filter(available=True)
    else:
        products = Product.objects.filter(available=True, brnd_id=id)
    if products.count():
        return render(request, 'shop.html', context={'menu': menu,
                                                     'num_el': 2,
                                                     'brands': brands,
                                                     'brand': brand,
                                                     'categories': categories,
                                                     'lines': lines,
                                                     'products': products,
                                                     'cart': cart})
    else:
        return  HttpResponse('Нема на складі')

def line_view(request,  id):
    cart = Cart(request)
    line = get_object_or_404(Product, id=id, available=True)
    products = Product.objects.filter(available=True, line_id=id)
    if products.count():
        return render(request, 'shop.html', context={'menu': menu,
                                                     'num_el': 4,
                                                     'brands': brands,
                                                     'line': line,
                                                     'categories': categories,
                                                     'lines': lines,
                                                     'products': products,
                                                     'cart': cart})
    else:
        return  HttpResponse('Нема на складі')

def cat_view(request,  id):
    cart = Cart(request)
    category = get_object_or_404(Product, id=id, available=True)
    products = Product.objects.filter(available=True, cat_id=id)
    if products.count():
        return render(request, 'shop.html', context={'menu': menu,
                                                     'num_el': 3,
                                                     'brands': brands,
                                                     'category': category,
                                                     'categories': categories,
                                                     'lines': lines,
                                                     'products': products,
                                                     'cart': cart})
    else:
        return  HttpResponse('Нема на складі')


def product_detail(request, id, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop-single.html', {'menu': menu,
                                                'num_el': 2,
                                                'brands': brands,
                                                'categories': categories,
                                                'lines': lines,
                                                'products': products,
                                                'product': product,
                                                'cart': cart, })

def cart_view(request):

    cart = Cart(request)
    return render(request, 'cart.html', context={'menu': menu,
                                                 'num_el': 2,
                                                 'brands': brands,
                                                 'categories': categories,
                                                 'lines': lines,
                                                 'products': products,
                                                 'cart': cart, })


# def product_list(request, category_slug=None):
#     cart = Cart(request)
#     products = Product.objects.filter(available=True)
#     return render(request, 'list.html', {'products': products, 'cart': cart})
