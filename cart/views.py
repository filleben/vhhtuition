from django.shortcuts import render, redirect, reverse


def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, id):
    quantity = 1
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(reverse('view_cart'))


def remove_item(request, id):
    cart = request.session.get('cart', {})
    quantity = cart[id] - 1

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart

    return redirect(reverse('view_cart'))
