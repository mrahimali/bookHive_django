from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from store.models import BookInfo


class Cart(View):
    def get(self , request):
        cart=request.session.get('cart')
        ids=list(cart.keys())
        books=BookInfo.get_books_by_ids(ids)
        return render(request, 'cart.html', {'books':books})