from django.urls import path
from .views import home, signup, login, cart, profile, edit_profile

urlpatterns = [
    path('', home.home.as_view(), name='homepage' ),
    path('cart/', cart.Cart.as_view(), name='cart'),
    path('profile/', profile.Profile.as_view(), name='profile'),
    path('edit-profile/', edit_profile.EditProfile.as_view(), name='editprofile'),
    path('signup/', signup.SignUp.as_view(), name='signup'),
    path('login/', login.Login.as_view(), name='login'),
    path('logout/', login.logout, name='logout')
    
]
