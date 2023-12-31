from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from main_page.views import menu


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'thankyou.html',
                          {'order': order, 'menu': menu, 'num_el': 1})

    else:
        form = OrderCreateForm
    return render(request, 'checkout.html',
                  {'cart': cart, 'form': form, 'menu': menu, 'num_el': 2})
