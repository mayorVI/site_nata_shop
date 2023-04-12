from django.shortcuts import render
from shop.models import Product, Brand, Category, Line
from cart.cart import Cart
from contact.forms import LetterForm


# Create your views here.

menu = [{'title': 'Головна', 'url_name': 'main_page'},
        {'title': 'Товари', 'url_name': 'shop:shop'},
        {'title': 'Бренди', 'url_name': 'shop:shop'},
        {'title': 'Типи', 'url_name': 'shop:shop'},
        {'title': 'Лінійки', 'url_name': 'sysderma'},
        {'title': 'Контакти', 'url_name': 'contact'},
]
brands = Brand.objects.filter(available=True)
def main_page(request):

    cart = Cart(request)
    products = Product.objects.filter(available=True, popular=True)
    newest = Product.objects.filter(available=True, popular=False)
    return render(request, 'main_page.html', context={'menu': menu,
                                                      'num_el': 1,
                                                      'brands': brands,
                                                      'products': products,
                                                      'newest': newest,
                                                      'cart': cart, })



def sysderma(request):

    return render(request, 'thankyou.html', context={'menu': menu,
                                                     'num_el': 5, })


def contact(request):

    cart = Cart(request)

    if request.method == 'POST':
        letter_form = LetterForm(request.POST)
        if letter_form.is_valid():
            letter_form.save()
            return render(request, 'thankyou.html', context={'menu': menu,
                                                             'num_el': 5, })
    else:
        letter_form = LetterForm()
    return render(request, 'contact.html', context={'menu': menu,
                                                    'num_el': 6,
                                                    'letter_form': letter_form,
                                                    'cart': cart,
                                                    'brands': brands,
                                                    })

