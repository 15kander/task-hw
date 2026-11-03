from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import OrderForm
def getreq(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            prod_val = form.cleaned_data.get('product')
            prod_lab = dict(form.fields['product'].choices).get(prod_val)
            del_val = form.cleaned_data.get('delivery')
            del_lab = dict(form.fields['delivery'].choices).get(del_val)
            request.session['order_data'] = {
                'name' : request.POST.get('name'),
                "phone": request.POST.get('phone'),
                'product_val' : int(prod_val),
                'product_name' : prod_lab,
                'quant' : request.POST.get('quantity'),
                'delivery_val' : int(del_val),
                'delivery_name' : del_lab,
                'adrs' : request.POST.get('address'),
            }
            return redirect('ordresult')
    else:
        orderform = OrderForm()
        return render(request, "order.html", {"form": orderform})

def ordresult(request):
    ord = request.session.get('order_data',{})
    if not ord:
        return HttpResponse('Данные не найдены. Заполните форму заново')
    price = ord.get('product_val',0)
    delivery = ord.get('delivery_val',0)
    quantity = ord.get('quant',0)
    total = price * int(quantity)+delivery
    return HttpResponse(f"""
        <h1>Order Check</h1>
        <h2>Buyer: {ord.get('name')}</h2>
        <h2>Product: {ord.get('product_name')}</h2>
        <h2>Quantity: {quantity}</h2>
        <h2>Price per piece: {price} uzs</h2>
        <h2>Delivery: {ord.get('delivery_name')}</h2>
        <h2>Total:</h2>
        <h2>{str(total)} uzs</h2>
        
    """)