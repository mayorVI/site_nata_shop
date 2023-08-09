from .models import *

brands = Brand.objects.filter(available=True)
categories = Category.objects.filter(available=True)
lines = Line.objects.filter(available=True)

menu = [{'title': 'Головна', 'url_name': 'main_page'},
        {'title': 'Бренди', 'url_name': 'shop:brands'},
        {'title': 'Типи',   'url_name': 'shop:categories'},
        {'title': 'Лінійки', 'url_name': 'shop:lines'},
        {'title': 'Контакти', 'url_name': 'contact'},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['brands'] = brands
        context['categories'] = categories
        context['lines'] = lines
        # if 'num_el' not in context:
        #     context['num_el'] = 1
        return context
