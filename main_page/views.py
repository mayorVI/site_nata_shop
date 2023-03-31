from django.shortcuts import render, redirect

# Create your views here.

menu = [{'title': 'Головна', 'url_name': 'main_page'},
        {'title': 'Товари', 'url_name': 'shop:shop'},
        {'title': 'Sysderma', 'url_name': 'sysderma'},
        {'title': 'Контакт', 'url_name': 'contact'},
]

def main_page(request):

    return render(request, 'main_page.html', context={'menu': menu,
                                                      'num_el': 1, })


def shop(request):

    return render(request, 'shop.html', context={'menu': menu,
                                                 'num_el': 2, })


def sysderma(request):

    return render(request, 'thankyou.html', context={'menu': menu,
                                                     'num_el': 3, })


def contact(request):

    return render(request, 'contact.html', context={'menu': menu,
                                                    'num_el': 4, })
