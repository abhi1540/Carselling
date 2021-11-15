from django.shortcuts import render
from django.views import View
from .models import Team
from cars.models import Car


class Home(View):
    template_name = 'home.html'
    teams = Team.objects.all()
    cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars = Car.objects.order_by('-created_date')
    search_fields = Car.objects.values('model', 'city', 'year', 'body_style', 'price')
    model_val_search = Car.objects.values('model').distinct()
    city_val_search = Car.objects.values('city').distinct()
    year_val_search = Car.objects.values('year').distinct()
    body_style_val_search = Car.objects.values('body_style').distinct()

    data = {
        'teams': teams,
        'featured_car': cars,
        'latest_cars' : latest_cars,
        'search_fields': search_fields,
        'model_val_search': model_val_search,
        'city_val_search': city_val_search,
        'year_val_search': year_val_search,
        'body_style_val_search': body_style_val_search,
    }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.data)



class About(View):
    template_name = 'about.html'
    teams = Team.objects.all()
    data = {
        'teams': teams
    }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.data)


class Services(View):
    template_name = 'services.html'
    def get(self, request):
        return render(request, self.template_name)


class Contact(View):
    template_name = 'contact.html'
    def get(self, request):
        return render(request, self.template_name)