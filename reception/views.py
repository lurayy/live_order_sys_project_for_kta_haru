from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from menu.models import Order, OrderedItem
import json
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

@login_required
def get_order(request):
    orders = Order.objects.all()
    response = {'order':[]}
    for order in orders:
        json_order = {'name':[],'price':[],'id':int(order.id)}
        json_order['table_number'] = str(order.table_number)
        json_order['timestamp'] = order.timestamp
        if not order.is_done:     
            ordered_items = OrderedItem.objects.all().filter(order = order)
            for ordered_item in ordered_items:
                json_order['name'].append(ordered_item.food_item.name)
                json_order['price'].append(ordered_item.food_item.price)
            response['order'].append(json_order)
    return render(request, 'reception/reception.html', {'orders': response})

@login_required
def order_done(request):
    if request.method == "POST":
        json_str = request.body.decode(encoding= 'UTF-8')
        data = json.loads(json_str)
        order = Order.objects.get(id=int(data))
        order.is_done = True
        order.save()
    return HttpResponse("Done")

# def login_user(request):
#     if request.method == "POST":
#         username = request.body['username']
#         password = request.body['password']
#         login(username,password)
 