from django.shortcuts import render
from django.views import View
from .models import Team


class Home(View):
    template_name = 'home.html'
    teams = Team.objects.all()
    data = {
        'teams': teams
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