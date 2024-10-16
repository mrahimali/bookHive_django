from django.urls import path
from .views import home, signup, login, cart, profile, edit_profile, book, order

urlpatterns = [
    path('', home.home.as_view(), name='homepage' ),
    path('cart/', cart.Cart.as_view(), name='cart'),
    path('profile/', profile.Profile.as_view(), name='profile'),
    path('edit-profile/', edit_profile.EditProfile.as_view(), name='editprofile'),
    path('edit-book/<int:bookId>', book.EditBook.as_view(), name='edit-book'),
    path('profile/delete-address/<int:id>', profile.delete_address, name='delete-address'),
    path('profile/delete-book/<int:id>', profile.delete_book, name='delete_book'),
    path('add-book/', book.AddBook.as_view(), name='add-book'),
    path('place-order/', order.Orders.as_view(), name='placeorder'),
    path('orders/', order.Orders.as_view(), name='orders'),
    path('order-confirm', order.OrderConfirm.as_view(),name='order_confirmation'),
    path('signup/', signup.SignUp.as_view(), name='signup'),
    path('login/', login.Login.as_view(), name='login'),
    path('logout/', login.logout, name='logout')
    
]
