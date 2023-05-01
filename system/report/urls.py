from django.contrib import admin
from django.urls import path
from .views import homeView, detailView, categoryView

urlpatterns = [
    # detail
    path('',homeView,name='home_url'),
    path('<slug:slug>/<int:pk>', detailView, name='detail_url'),
    path('<slug:slug>/', categoryView, name='category_url'),
]
