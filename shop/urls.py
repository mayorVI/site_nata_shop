from django.urls import path
from . import views
from main_page.views import shop

app_name = 'shop'

urlpatterns = [
    path('', shop, name='shop'),
#    path('', views.product_list, name='product_list'),
#    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]