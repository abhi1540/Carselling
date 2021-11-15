from django.urls import path, include
from cars.views import Cars, Cars_Details, Search
urlpatterns = [
    path('', Cars.as_view(), name='cars'),
    path('<int:id>', Cars_Details.as_view(), name='car-details'),
    path('search', Search.as_view(), name='search')

]
