from django.urls import path, include
from .views import RegisterClient, LoginClient, RegisterView, LoginView

urlpatterns = [
    path('registerUser/', RegisterView.as_view(), name='register_user'),
    path('loginUser/', LoginView.as_view(), name='login_user'),
    #path('user/', UserView.as_view(), name='user'),
    #path('logout/', LogoutView.as_view(), name='logout_user'),
    #path('register/', RegisterUser.as_view(), name='register'),
    path('register/', RegisterClient.as_view(), name='regiter'),
    path('login/', LoginClient.as_view(), name='login')
]

#prueba@gmail.com
#prueba2003