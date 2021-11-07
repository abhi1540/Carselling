from django.urls import path, include

from .views import Home, About, Services, Contact
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about', About.as_view(), name='about'),
    path('services', Services.as_view(), name='services'),
    path('contact', Contact.as_view(), name='contact'),
]
