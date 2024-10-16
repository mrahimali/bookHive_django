from django.views import View
from django.shortcuts import redirect, render
from store.models import Order, BookInfo, OrderItem, ShippingAddresses, UserDetail



class Orders(View):
    def get(self, request):
        user_id = request.session.get('id')
        if user_id is None:
            return redirect('login')  

        my_ordered_books = OrderItem.objects.filter(product_owner_id=user_id)

        purchased_books = OrderItem.objects.filter(order__ordered_by_id=user_id)

        context = {
            'my_ordered_books': my_ordered_books,
            'purchased_books': purchased_books
        }
        return render(request, 'order.html', context)



    def post(self, request):
        address_id = request.POST.get('selected_address')
        cart = request.session.get('cart', {})

        # Check if the user is logged in
        user_id = request.session.get('id')  # Get user ID from session
        if not user_id:
            return redirect('login')  # Redirect to login if user is not authenticated

        # Get the current user using the ID stored in the session
        user = UserDetail.objects.get(id=user_id)

        # If the cart is empty, redirect to the cart page
        if not cart:
            return redirect('cart')

        # Retrieve the selected shipping address
        try:
            shipping_address = ShippingAddresses.objects.get(id=address_id)
        except ShippingAddresses.DoesNotExist:
            return redirect('cart')  # Handle case where address does not exist

        total_amount = 0.00
        for book_id, quantity in cart.items():
            # Get the book information
            try:
                book = BookInfo.objects.get(id=book_id)
                total_amount += book.price * quantity  # Sum up the total amount
            except BookInfo.DoesNotExist:
                continue  # Handle case where book does not exist

        # Create the Order instance
        order = Order.objects.create(
            ordered_by=user,
            total_amount=total_amount,
            shipping_address=shipping_address
        )

        # Create OrderItem instances for each book in the cart
        for book_id, quantity in cart.items():
            book = BookInfo.objects.get(id=book_id)
            product_owner = book.uploaded_by

            # Create an order item for the current book
            OrderItem.objects.create(
                order=order,
                product=book,
                quantity=quantity,
                product_owner=product_owner,
                price=book.price  # Store the price of the book at the time of order
            )

        # Clear the shopping cart after placing the order
        request.session['cart'] = {}

        # Redirect to an order confirmation page
        return redirect('order_confirmation')
    

class OrderConfirm(View):
    def get(self, request):
        return render(request, 'confirm.html')