from django import template

register=template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(book, cart):
    # cart.keys()
    for id in cart.keys():
        if int(id)==book.id:
            return True
    return False


@register.filter(name='cart_quantity')
def cart_quantity(book, cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==book.id:
            return cart.get(id)
    return 0



@register.filter(name='get_no_of_item')
def get_no_of_item(book_id, cart):
    if cart is not None:
        return cart.get(str(book_id), 0)  # Return 0 if book_id not found in the cart
    return 0  # Return 0 if the cart is None


@register.filter(name='price_symbol')
def price_symbol(price):
    return f"₹{price}"


@register.filter(name='total_price')
def total_price(qty, price):
    if qty is None:
        qty = 0  # Ensure qty defaults to 0
    return int(qty) * int(price)


@register.filter(name='grandTotal')
def grandTotal(books, cart):
    total = 0
    if cart:
        for book in books:
            qty = cart.get(str(book.id),0)  # Get the quantity from cart or 0 if not found
            # qty = cart.get(book.id,0)
            total += int(book.price) * int(qty)         # Multiply book price by the quantity
        return total
    else:
        return "No cart found"

    
    