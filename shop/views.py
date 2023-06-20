from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.db.models import Q
from django.views.generic import ListView
from django.core.paginator import Paginator

from .models import *
from cart.cart import Cart
from main_page.views import menu, lines, brands, categories


products = Product.objects.filter(available=True)

class ProductList(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 50
    page_kwarg = 'page'

    def get_context_data(self, *, object_list=None, **kwargs):
        cart = Cart(self.request)
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['num_el'] = 2
        context['brands'] = brands
        context['categories'] = categories
        context['lines'] = lines
        context['cart'] = cart
        return context

    def get_queryset(self):
        return Product.objects.filter(available=True)

class BrandProductList(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        cart = Cart(self.request)
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['num_el'] = 2
        context['brands'] = brands
        context['categories'] = categories
        context['lines'] = lines
        context['cart'] = cart
        return context

    def get_queryset(self):
        if self.kwargs['brand_slug'] == 'vsi':
            return Product.objects.filter(available=True)
        else:
            return Product.objects.filter(brnd__slug=self.kwargs['brand_slug'], available=True)
class LineProductList(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        cart = Cart(self.request)
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['num_el'] = 4
        context['brands'] = brands
        context['categories'] = categories
        context['lines'] = lines
        context['cart'] = cart
        return context

    def get_queryset(self):
        return Product.objects.filter(line__slug=self.kwargs['line_slug'], available=True)

class CatProductList(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        cart = Cart(self.request)
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['num_el'] = 3
        context['brands'] = brands
        context['categories'] = categories
        context['lines'] = lines
        context['cart'] = cart
        return context

    def get_queryset(self):
        return Product.objects.filter(cat__slug=self.kwargs['category_slug'], available=True)


def shop_sort_view(request, id=1):
    cart = Cart(request)
    if id == 1:
        sort_products = Product.objects.filter(available=True).order_by('name')
    elif id == 2:
        sort_products = Product.objects.filter(available=True).order_by('-name')
    elif id == 3:
        sort_products = Product.objects.filter(available=True).order_by('price')
    elif id == 4:
        sort_products = Product.objects.filter(available=True).order_by('-price')
    else:
        sort_products = Product.objects.filter(available=True)

    return render(request, 'shop.html', context={'menu': menu,
                                                 'num_el': 2,
                                                 'brands': brands,
                                                 'categories': categories,
                                                 'lines': lines,
                                                 'products': sort_products,
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
        return HttpResponse('Нема на складі')

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


def cat_view(request,  slug):
    cart = Cart(request)
    category = get_object_or_404(Product, slug=slug, available=True)
    products = Product.objects.filter(available=True, cat__slug=slug)
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

def search_view(request):
    query = request.GET.get('q')
    object_list = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query))
    if object_list.count():
        return render(request, 'search_result.html', context={
                     'text_query': query,
                     'products': object_list})
    else:
        return  HttpResponse('Нема на складі')

