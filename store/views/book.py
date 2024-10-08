from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from store.models import BookInfo, Category, UserDetail

class EditBook(View):
    def get(self, request, bookId):
        book=BookInfo.objects.get(id=bookId)
        category= Category.objects.all()
        return render(request, 'edit-book.html', {'book':book, 'category':category})
    
    def post(self, request, bookId):
        book = get_object_or_404(BookInfo, id=bookId)
        postData=request.POST
        book.title=postData.get('title')
        book.price=postData.get('price')
        book.description=postData.get('description')
        category_id = postData.get('category') 
        if category_id:
            category_instance = get_object_or_404(Category, id=category_id)
            book.category = category_instance
        book.writer=postData.get('writer')
        if request.FILES.get('book_image'):
            book.book_image = request.FILES['book_image']

        book.save()
        return redirect('profile')


class AddBook(View):
    def get(self, request):
        category= Category.objects.all()
        return render(request, 'add-book.html', { 'category':category})
    

    def post(self, request):
        postData=request.POST

        title=postData.get('title')
        price=postData.get('price')
        description=postData.get('description')
        category_id = postData.get('category') 
        if category_id:
            category_instance = get_object_or_404(Category, id=category_id)
            category = category_instance
        writer=postData.get('writer')
        book_image=request.FILES.get('book_image')
        uploaded_by=request.session['id']
        if uploaded_by:
            user_instance = get_object_or_404(UserDetail, id=uploaded_by)
            uploaded_by = user_instance

        filled_values={
            'title':title,
            'price':price,
            'description':description,
            'category':category,
            'writer':writer,
            'book_image':book_image,
        }

        error_message=None
        
        book=BookInfo(
            title=title,
            price=price,
            description=description,
            category=category,
            writer=writer,
            uploaded_by=uploaded_by,
            book_image=book_image
        )

        error_message=self.validateBookInfo(book)

        if not error_message:
            book.add_book()
            return redirect('homepage')
        else:
            data={
                'error_message':error_message,
                'values':filled_values
            }
            return redirect(request,'add-book.html', data)






    def validateBookInfo(self, book):
        error_message=None
        if not book.title:
            error_message="Title Required!!"
        elif not book.price:
            error_message="Price Required!!!"
        elif not book.description:
            error_message="Description Required!!"
        elif not book.category:
            error_message="Please Selecte Category !!"
        elif not book.writer:
            error_message="Please provide writer name !!"
        elif not book.book_image:
            error_message="Upload Image !!"
        
        return error_message

