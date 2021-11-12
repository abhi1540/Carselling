from django.urls import path, include
from cars.views import Cars
urlpatterns = [
path('', Cars.as_view(), name='cars'),
]
