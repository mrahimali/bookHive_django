from django.shortcuts import render
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