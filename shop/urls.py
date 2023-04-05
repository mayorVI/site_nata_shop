from django.urls import path
from . views import *


app_name = 'shop'

urlpatterns = [
    path('', shop_view, name='shop'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('cart/', cart_view, name='cart_view'),
]