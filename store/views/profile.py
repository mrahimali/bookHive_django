from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from store.models import UserDetail, BookInfo


class Profile(View):
    def get(self, request):
        userEmail=request.session['userEmail']
        user= UserDetail.get_user_by_email(userEmail)
        books=BookInfo.get_books_by_owner_id(request.session['id'])
        return render(request, 'profile.html', {'user':user, 'books':books})