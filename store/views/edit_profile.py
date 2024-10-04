from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from store.models import UserDetail



class EditProfile(View):
    def get(self, request):
        userEmail=request.session['userEmail']
        user=UserDetail.get_user_by_email(userEmail)
        return render(request, 'editprofile.html', {'user':user})
    
    def post(self , request):
        userEmail=request.session['userEmail']
        user=UserDetail.get_user_by_email(userEmail)


        postData= request.POST

        name=postData.get('name')
        email=postData.get('email')
        phone=postData.get('phone')
        account_type=postData.get('account_type')

        filledValues={
            'name':name,
            'email':email,
            'phone':phone,
            'account_type':account_type
        }
        error_message=self.validateUser(filledValues)

        if not error_message:
            user.name=name
            user.email=email
            user.phone=phone
            user.user_type=account_type
            user.save()
            request.session['userEmail']=email
            return redirect('profile')
        else:
            data={
                'values':filledValues,
                'error_message':error_message
            }
            return render(request, 'editprofile.html', data)

        


    def validateUser(self, filledValues):
        error_message=None
        if not filledValues.get('name'):
            error_message='Name Required !!'
        elif not filledValues.get('email'):
            error_message='Email Required !!'
        elif not filledValues.get('phone'):
            error_message='Phone number required'
        elif len(filledValues.get('phone'))<10 or len(filledValues.get('phone'))>14:
            error_message="Invalid Phone number !!!"
        elif not filledValues.get('account_type'):
            error_message="Please select account type !!!"

        return error_message