from django.urls import path, include
from .views import *


urlpatterns = [
    path('', main_page, name='main_page'),
    path('contact/', contact, name='contact'),
    path('shop/', include('shop.urls')),
    path('sysderma/', sysderma, name='sysderma')
]
