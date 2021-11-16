from django.contrib import admin
from django.urls import path, include
from .views import Contacts


urlpatterns = [
    path('inquiry/', Contacts.as_view(), name='inquiry'),
]