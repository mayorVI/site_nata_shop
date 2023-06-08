from django.shortcuts import render,redirect
from contact.models import Letter
from orders.models import Order, OrderItem
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.groups.filter(name='manager').exists()


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def letters_view(request):
    letters = Letter.objects.all()
    return render(request, 'list_letters.html', context={'letters': letters, 'title': 'Отримані сповіщення'})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def letters_update(request, pk):
    letters = Letter.objects.filter(pk=pk).update()
    return redirect(request, 'list_letters.html', context={'letters': letters, 'title': 'Отримані сповіщення'})



@login_required(login_url='/login/')
def orders_view(request):
    orders = Order.objects.all()
    orderitems = OrderItem.objects.all()
    return render(request, 'order_list.html', context={'orders': orders,
                                                       'orderitems': orderitems,
                                                       'title': "Отримані замовлення"})

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_order(request, pk):
    Order.objects.filter(pk=pk).update(paid=True)
    return redirect('manager:orders')


