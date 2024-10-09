from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from store.models import BookInfo, UserDetail, ShippingAddresses


class Cart(View):
    def get(self , request):
        cart=request.session.get('cart')
        ids=list(cart.keys())
        books=BookInfo.get_books_by_ids(ids)
        return render(request, 'cart.html', {'books':books})
    

    def post(self, request):
        book_id = request.POST.get('book_id') or request.POST.get('increment') or request.POST.get('decrement')
        

        cart = request.session.get('cart', {})
        if book_id:
            if request.POST.get('decrement'):
                qty = cart.get(book_id, 0)
                if qty > 1:
                    cart[book_id] = qty - 1
                else:
                    cart.pop(book_id)
            else:
                cart[book_id] = cart.get(book_id, 0) + 1

        request.session['cart'] = cart
        print(request.session['cart'])

        return redirect('cart')
    

# class Checkout(View):
#     def get(self , request):
#         cart=request.session.get('cart')
#         user_id=request.session['id']
#         user=UserDetail.objects.get(id=user_id)
#         adrresses= ShippingAddresses.objects.filter(details_of=user.id)
#         ids=list(cart.keys())
#         books=BookInfo.get_books_by_ids(ids)
#         data={
#             'books':books,
#             'user':user,
#             'address':adrresses
#         }
#         return render(request, 'checkout.html', data)