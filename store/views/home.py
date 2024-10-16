from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from store.models import BookInfo , Category


class home(View):

    def get(self, request):
        
        categories=Category.get_all_category()
        category_id=request.GET.get('category')
        if category_id:
            books=BookInfo.get_books_by_category(category_id)
            return render(request, 'home.html', {'books':books, 'categories':categories})
        else:
            books=BookInfo.get_all_books()
            return render(request, 'home.html', {'books':books, 'categories':categories})
        
        
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

        return redirect('/')



    