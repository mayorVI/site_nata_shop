from django.shortcuts import render
from shop.models import Product
from cart.cart import Cart
from contact.forms import LetterForm
from contact.models import Letter

# Create your views here.

menu = [{'title': 'Головна', 'url_name': 'main_page'},
        {'title': 'Товари', 'url_name': 'shop:shop'},
        {'title': 'Sysderma', 'url_name': 'sysderma'},
        {'title': 'Контакт', 'url_name': 'contact'},
]

def main_page(request):

    cart = Cart(request)
    products = Product.objects.filter(available=True, popular=True)
    newest = Product.objects.filter(available=True, popular=False)
    return render(request, 'main_page.html', context={'menu': menu,
                                                      'num_el': 1,
                                                      'products': products,
                                                      'newest': newest,
                                                      'cart': cart, })



def sysderma(request):

    return render(request, 'thankyou.html', context={'menu': menu,
                                                     'num_el': 3, })


def contact(request):

    cart = Cart(request)
    letter_form = LetterForm(request)

    if request.method == 'POST':
        letter_form = LetterForm(request.POST)
        if letter_form.is_valid():
            letter_form.save()
            return render(request, 'thankyou.html', context={'menu': menu,
                                                             'num_el': 3, })
    else:
        letter_form = LetterForm()
    return render(request, 'contact.html', context={'menu': menu,
                                                    'num_el': 4,
                                                    'letter_form': letter_form,
                                                    'cart': cart, })

