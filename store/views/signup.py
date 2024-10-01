from django.shortcuts import render, redirect
from django.views import View
from store.models import UserDetail
from django.contrib.auth.hashers import make_password



class SignUp(View):
    
    def get(self, request):
        return render(request, 'signup.html')
    

    def post(self, request):
        postData=request.POST
        name=postData.get('name')
        email=postData.get('email')
        phone=postData.get('phone')
        account_type=postData.get('account_type')
        password=postData.get('password')
        cpassword=postData.get('cpassword')

        filledValues={
            'name':name,
            'email':email,
            'phone':phone,
            'user_type':account_type
        }


        user =UserDetail(
            name=name,
            phone=phone,
            email= email,
            password=password,
            user_type=account_type
        )
        error_message=self.validateUser(user)

        if not error_message:
            if password==cpassword:
                user.password=make_password(user.password)
                user.registerUser()
                return redirect('homepage')
                

            else:
                error_message="password and confirm password did not match"
                data={
                    'values':filledValues,
                    'error_message':error_message
                }
                return render(request, 'signup.html', data)
        else:
            data={
                'values':filledValues,
                'error_message':error_message
            }
            return render(request, 'signup.html', data)

    
    def validateUser(self, user):
        error_message=None
        if not user.name:
            error_message='Name Required !!'
        elif not user.email:
            error_message='Email Required !!'
        elif not user.phone:
            error_message='Phone number required'
        elif len(user.phone)<10 or len(user.phone)>14:
            error_message="Invalid Phone number !!!"
        elif not user.user_type:
            error_message="Please select account type !!!"

        return error_message
