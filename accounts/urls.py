from django.urls import path, include
from .views import Login, Registration, Logout, Dashboard
urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('registration', Registration.as_view(), name='registration'),
    path('logout', Logout.as_view(), name='logout'),
    path('dashboard', Dashboard.as_view(), name='dashboard'),


]
