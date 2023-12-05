from django.urls import path, include
from .views import RegisterClient, LoginClient

urlpatterns = [
    #path('register_user/', RegisterView.as_view(), name='register_user'),
    #path('login/', LoginView.as_view(), name='login_user'),
    #path('user/', UserView.as_view(), name='user'),
    #path('logout/', LogoutView.as_view(), name='logout_user'),
    #path('register/', RegisterUser.as_view(), name='register'),
    path('register/', RegisterClient.as_view(), name='regiters'),
    path('login/', LoginClient.as_view(), name='log')
]