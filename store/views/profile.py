from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from store.models import UserDetail, BookInfo, ShippingAddresses
from django.contrib import messages 

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
        name=postData.get('name')
        city=postData.get('city')
        phone=postData.get('phone')
        id=request.session['id']
        if id:
            user_instance = get_object_or_404(UserDetail, id=id)

        address=ShippingAddresses(
            address=address,
            name=name,
            city=city,
            phone=phone,
            details_of= user_instance
        )

        error_message=None
        error_message=self.validate_address(address)

        if not error_message:
            address.addAddress()
            return redirect('profile')
        else:

            # from django.db.models import Prefetch

            # userEmail = request.session['userEmail']
            # user = UserDetail.objects.prefetch_related(
            #     Prefetch('bookinfo_set', queryset=BookInfo.objects.filter(owner_id=request.session['id'])),
            #     Prefetch('shippingaddresses_set')
            # ).get(email=userEmail)

            # # Now, user.books and user.addresses are already prefetched with optimized queries
            # books = user.bookinfo_set.all()  # No need for extra query
            # addresses = user.shippingaddresses_set.all()  # No need for extra query

            # data = {
            #     'user': user,
            #     'books': books,
            #     'addresses': addresses,
            #     'error_message': error_message
            # }

            # messages.success(request, 'Address added!!!')
            # return redirect('profile')

            userEmail=request.session['userEmail']
            user= UserDetail.get_user_by_email(userEmail)
            books=BookInfo.get_books_by_owner_id(request.session['id'])
            addresses=ShippingAddresses.get_address_by_id(user.id)
            data={'user':user, 'books':books, 'addresses':addresses, 'error_message':error_message}
            messages.success(request, 'Address added!!!')
            return redirect('profile')
            # return render(request,'profile.html', data)
    

    def validate_address(self, address):
        error_message=None
        if not address.address:
            error_message="Please provide address!!"
        elif not address.name:
            error_message="Please enter receiver's name!!"
        elif not address.city:
            error_message="Enter city !!!"
        elif not address.phone:
            error_message="Please enter your mobile number"
        elif len(address.phone)<10 or len(address.phone)>10:
            error_message="Invalid Mobile number in address form !!"
        return error_message
    
def delete_address(request, id):
    if request.method == 'POST':
        address = ShippingAddresses.objects.get(id=id)
        address.delete()
        messages.success(request, 'Address deleted successfully.')  # Add success message
        return redirect('profile')  # Redirect to some page after deletion
    

def delete_book(request, id):
    
    book=BookInfo.objects.get(id=id)
    if book:
        book.delete()
        messages.success(request, 'Book deleted successfully !!!')
        return redirect('profile')
    else:
        messages.warning(request, 'Book did not delete....Try again !!!')
        return redirect('profile')

