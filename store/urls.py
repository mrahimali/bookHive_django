from django.urls import path
from .views import home, signup, login, cart, profile, edit_profile, book

urlpatterns = [
    path('', home.home.as_view(), name='homepage' ),
    path('cart/', cart.Cart.as_view(), name='cart'),
    path('profile/', profile.Profile.as_view(), name='profile'),
    path('edit-profile/', edit_profile.EditProfile.as_view(), name='editprofile'),
    path('edit-book/<int:bookId>', book.EditBook.as_view(), name='edit-book'),
    path('add-book/', book.AddBook.as_view(), name='add-book'),
    path('signup/', signup.SignUp.as_view(), name='signup'),
    path('login/', login.Login.as_view(), name='login'),
    path('logout/', login.logout, name='logout')
    
]
