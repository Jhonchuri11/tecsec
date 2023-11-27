from django.urls import path, include
from .views import RegisterView, LoginView, UserView, LogoutView
from rest_framework import routers


urlpatterns = [
    path('register_user/', RegisterView.as_view(), name='register_user'),
    path('login/', LoginView.as_view(), name='login_user'),
    path('user/', UserView.as_view(), name='user'),
    path('logout/', LogoutView.as_view(), name='logout_user')
]