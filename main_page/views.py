from django.shortcuts import render
from shop.models import Product, Brand, Category, Line
from cart.cart import Cart
from contact.forms import LetterForm
from contact.models import Letter
from orders.models import Order, OrderItem


# Create your views here.

menu = [{'title': 'Головна', 'url_name': 'main_page'},
        {'title': 'Бренди', 'url_name': 'shop:brands'},
        {'title': 'Типи',   'url_name': 'shop:categories'},
        {'title': 'Лінійки', 'url_name': 'shop:lines'},
        {'title': 'Контакти', 'url_name': 'contact'},
]
brands = Brand.objects.filter(available=True)
categories = Category.objects.filter(available=True)
lines = Line.objects.filter(available=True)
def main_page(request):

    cart = Cart(request)
    products = Product.objects.filter(available=True, popular=True)
    newest = Product.objects.filter(available=True, popular=False)
    return render(request, 'main_page.html', context={'menu': menu,
                                                      'num_el': 1,
                                                      'brands': brands,
                                                      'categories': categories,
                                                      'lines': lines,
                                                      'products': products,
                                                      'newest': newest,
                                                      'cart': cart, })



def contact(request):

    cart = Cart(request)

    if request.method == 'POST':
        letter_form = LetterForm(request.POST)
        if letter_form.is_valid():
            letter_form.save()
            return render(request, 'thankyou.html', context={'menu': menu, 'num_el': 5,
})
    else:
        letter_form = LetterForm()
    return render(request, 'contact.html', context={'menu': menu,
                                                    'num_el': 5,
                                                    'letter_form': letter_form,
                                                    'cart': cart,
                                                    'brands': brands,
                                                    'categories': categories,
                                                    'lines': lines,
                                                    })


