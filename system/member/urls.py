from django.contrib import admin
from django.urls import path
from .views import loginView, registerView, logoutView

urlpatterns = [
    #users
    path('login/',loginView, name="login_url"),
    path('register/',registerView, name="register_url"),
    path('logout/',logoutView, name="logout_url"),
]
