from django.urls import path
from .views import home, signup, login, cart

urlpatterns = [
    path('', home.home.as_view(), name='homepage' ),
    path('cart/', cart.Cart.as_view(), name='signup'),
    path('signup/', signup.SignUp.as_view(), name='signup'),
    path('login/', login.Login.as_view(), name='login'),
    path('logout/', login.logout, name='logout')
]
