from django.shortcuts import render, redirect
from django.views import View
from store.models import UserDetail
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password



class Login(View):
    
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        postData=request.POST
        email=postData.get('email')
        password=postData.get('password')
        filled_values={
            'email':email
        }
        error_message=None

        user=UserDetail.get_user_by_email(email)
        if user:
            flag=check_password(password, user.password)
            if flag:
                request.session['id']=user.id
                request.session['userName']=user.name
                request.session['userEmail']=user.email
                request.session['userPhone']=user.phone
                request.session['userRole']=user.user_type
                return redirect('/')
            else:
                error_message="password did not match"
                data={
                    'error_message':error_message,
                    'values':filled_values
                }
                return render(request, 'login.html', data)
        else :
            error_message="user does not exist!!!"
            data={
                    'error_message':error_message,
                    'values':filled_values
                }
            return render(request, 'login.html', data)
        
    
def logout(request):
    request.session.clear()
    return redirect('login')

    

    