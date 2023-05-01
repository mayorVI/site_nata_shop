from django.urls import path
from . views import *


app_name = 'shop'

urlpatterns = [
    path('', shop_view, name='shop'),
    path('brand/', brands_view, name='brands'),
    path('brand/<int:id>/', brand_view, name='brand_products'),
    path('line/', lines_view, name='lines'),
    path('line/<int:id>/', line_view, name='line_products'),
    path('categories/', cats_view, name='categories'),
    path('categories/<int:id>/', cat_view, name='cat_products'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('cart/', cart_view, name='cart_view'),
]