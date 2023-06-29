from django.shortcuts import render, get_object_or_404, HttpResponse
from django.db.models import Q
from django.views.generic import ListView
from cart.cart import Cart

from .utils import *

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


class BrandProductList(DataMixin, ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        cart = Cart(self.request)
        context = super().get_context_data(**kwargs)
        context['num_el'] = 2
        context['cart'] = cart
        c_def = self.get_user_context(title='Бренди')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        if self.kwargs['brand_slug'] == 'vsi':
            return Product.objects.filter(available=True)
        else:
            return Product.objects.filter(brnd__slug=self.kwargs['brand_slug'], available=True)


class LineProductList(DataMixin, ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        cart = Cart(self.request)
        context = super().get_context_data(**kwargs)
        context['num_el'] = 4
        context['cart'] = cart
        c_def = self.get_user_context(title='Лінійки')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Product.objects.filter(line__slug=self.kwargs['line_slug'], available=True)


class CatProductList(DataMixin, ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        cart = Cart(self.request)
        context = super().get_context_data(**kwargs)
        context['num_el'] = 3
        context['cart'] = cart
        c_def = self.get_user_context(title='Типи')
        context = dict(list(context.items()) + list(c_def.items()))
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
        return HttpResponse('Нема на складі')
