from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, Order
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def showView(request):
    item = Item.objects.all()
    template_name = 'DemoApp/HomePage.html'
    context = {'item': item}
    return render(request, template_name, context)


# @login_required()
def CartView(request):
    all = Item.objects.all()
    print(all)
    if request.method == 'POST':
        itemS_id = request.POST.get('selected_item_id')
        print('***********', itemS_id)

        quantity = int(request.POST.get('quantity', 1))
        print('---', quantity)
        selected_item = Item.objects.get(pk=itemS_id)

        total_amount = selected_item.price * quantity
        print('total amount', total_amount)
        print(User.objects.all())


        # cart_item = {'id': selected_item.id, 'name': selected_item.name, 'quantity': quantity, 'price': selected_item.price ,'total_amount':total_amount}
        # print(cart_item)
        # cart_items = request.session.get('cart', [])
        # cart_items.append(cart_item)
        # request.session['cart'] = cart_items
        #
        # return redirect('cart')

        order = Order.objects.create(user=request.user)
        order_data = Order.objects.create(
            # order=order,
            user_id = order.user_id,
            item=selected_item.name,
            price_individual=selected_item.price,
            quantity=quantity,
            total_amount=total_amount,
        )
        order_data.save()
    # print('********orderdata',order_data)

    else:
        total_amount = 0
    template_name = 'DemoApp/CartPage.html'
    context = {'all': all, 'total_amount': total_amount}
    return render(request, template_name, context)



def finalPaymentView(request):
    # user_profile = None
    # if request.user.is_authenticated:
    #     user_profile = User.objects.get(user=request.user)

    order = Order.objects.filter(user=request.user)
    # for i in order:
    #     print(i)
    template_name = 'DemoApp/Final Paymentpage.html'
    context = {'order': order}
    return render(request, template_name, context)
