from django import template
from shop.models import *

register = template.Library()

@register.simple_tag()
def get_brands():
    return Brand.objects.all()

def get_lines():
    return Line.objects.all()

@register.inclusion_tag('list_products.html')
def show_products(filter=None, sort=None):
    if not filter:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(brnd_id=filter).order_by(sort)

    return {'products': products}