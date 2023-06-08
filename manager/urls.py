from django.urls import path
from .views import *

app_name = 'manager'

urlpatterns = [
    path('letters/', letters_view, name='letters'),
    path('orders/', orders_view, name='orders'),
    path('orders/update/<int:pk>/', update_order, name='update_order'),
]