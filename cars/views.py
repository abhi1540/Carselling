from django.shortcuts import render
from django.views import View
from .models import Car
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
# Create your views here.

class MyPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                # return the last page
                return self.num_pages
            elif int(number) < 1:
                # return the first page
                return 1
            else:
                raise




class Cars(View):
    template_name = 'cars.html'
    model = Car
    paginate_by = 4
    paginator_class = MyPaginator
    model_val_search = Car.objects.values('model').distinct()
    city_val_search = Car.objects.values('city').distinct()
    year_val_search = Car.objects.values('year').distinct()
    body_style_val_search = Car.objects.values('body_style').distinct()
    def get(self, request, *args, **kwargs):
        page = self.request.GET.get('page', 1)
        latest_cars = Car.objects.order_by('-created_date')
        paginator = self.paginator_class(latest_cars, self.paginate_by)

        latest_cars = paginator.page(page)
        data = {
            'latest_cars': latest_cars,
            'model_val_search': self.model_val_search,
            'city_val_search': self.city_val_search,
            'year_val_search': self.year_val_search,
            'body_style_val_search': self.body_style_val_search
        }
        return render(request, self.template_name, data)



class Cars_Details(View):
    template_name = 'car-details.html'
    model = Car
    def get(self, request, *args, **kwargs):
        single_car_detl = get_object_or_404(Car, pk=self.kwargs['id'])
        data = {
            'single_car_detl': single_car_detl
        }
        return render(request, self.template_name, data)



class Search(View):
    """https://learndjango.com/tutorials/django-search-tutorial"""
    template_name = "search.html"
    cars = Car.objects.order_by('-created_date')
    model_val_search = Car.objects.values('model').distinct()
    city_val_search = Car.objects.values('city').distinct()
    year_val_search = Car.objects.values('year').distinct()
    body_style_val_search = Car.objects.values('body_style').distinct()
    transmission_val_search = Car.objects.values('transmission').distinct()

    def get(self, request, *args, **kwargs):
        if "keyword" in request.GET:
            keyword = request.GET['keyword']
            if keyword:
                self.cars = self.cars.filter(
                    Q(car_title__icontains=keyword) |
                    Q(description__icontains=keyword)
                )

        if 'model' in request.GET:
            model = request.GET['model']
            if model:
                self.cars =  self.cars.filter(model__iexact=model)
        if 'city' in request.GET:
            city = request.GET['city']
            if city:
                self.cars  =   self.cars.filter(city__iexact=city)
        if 'year' in request.GET:
            year = request.GET['year']
            if year:
                self.cars =  self.cars.filter(year__iexact=year)
        if 'body_style' in request.GET:
            body_style = request.GET['body_style']
            if body_style:
                self.cars =  self.cars.filter(body_style__iexact=body_style)

        if 'transmission' in request.GET:
            transmission = request.GET['transmission']
            if transmission:
                self.cars =  self.cars.filter(transmission__iexact=transmission)

        if (('max_price' in request.GET) and
            ('min_price' in request.GET)):
            max_price = request.GET['max_price']
            min_price = request.GET['min_price']
            self.car = self.cars.filter(price__lte=max_price , price__gte = min_price)
        data = {
            'searched_data': self.cars,
            'model_val_search': self.model_val_search,
            'city_val_search': self.city_val_search,
            'year_val_search': self.year_val_search,
            'body_style_val_search': self.body_style_val_search,
            'transmission_val_search': self.transmission_val_search
        }
        return render(request, self.template_name, data)