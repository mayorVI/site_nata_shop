from django.urls import path
from .views import *

app_name = 'manager'

urlpatterns = [
    path('letters/', letters_view, name='letters'),
    path('orders/', orders_view, name='orders'),
]