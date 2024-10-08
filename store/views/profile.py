from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from store.models import UserDetail, BookInfo, ShippingAddresses


class Profile(View):
    def get(self, request):
        userEmail=request.session['userEmail']
        user= UserDetail.get_user_by_email(userEmail)
        books=BookInfo.get_books_by_owner_id(request.session['id'])
        addresses=ShippingAddresses.get_address_by_id(user.id)
        return render(request, 'profile.html', {'user':user, 'books':books, 'addresses':addresses})
    

    def post(self, request):
        postData=request.POST
        address=postData.get('address')
        phone=postData.get('phone')
        id=request.session['id']
        if id:
            user_instance = get_object_or_404(UserDetail, id=id)

        address=ShippingAddresses(
            address=address,
            phone=phone,
            details_of= user_instance
        )

        error_message=None
        error_message=self.validate_address(address)

        if not error_message:
            address.addAddress()
            return redirect('profile')
        else:
            userEmail=request.session['userEmail']
            user= UserDetail.get_user_by_email(userEmail)
            books=BookInfo.get_books_by_owner_id(request.session['id'])
            addresses=ShippingAddresses.get_address_by_id(user.id)
            data={'user':user, 'books':books, 'addresses':addresses, 'error_message':error_message}
            return render(request,'profile.html', data)
    

    def validate_address(self, address):
        error_message=None
        if not address.address:
            error_message="Please provide address!!"
        elif not address.phone:
            error_message="Please enter your mobile number"
        elif len(address.phone)<10 or len(address.phone)>10:
            error_message="Invalid Mobile number in address form !!"
        return error_message