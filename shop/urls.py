from django.urls import path
from . views import *


app_name = 'shop'

urlpatterns = [
    path('', ProductList.as_view(), name='shop'),
    path('search/', search_view, name='searching'),
    path('sort/<int:id>/', shop_sort_view, name='shop_sort'),
    path('brand/', brands_view, name='brands'),
    path('brand/<slug:brand_slug>/', BrandProductList.as_view(), name='brand_products'),
    path('line/', lines_view, name='lines'),
    path('line/<slug:line_slug>/', LineProductList.as_view(), name='line_products'),
    path('categories/', cats_view, name='categories'),
    path('categories/<slug:category_slug>/', CatProductList.as_view(), name='cat_products'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('cart/', cart_view, name='cart_view'),
]
