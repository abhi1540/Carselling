from django.shortcuts import render
from django.views import View
# Create your views here.


class Home(View):
    template_name = 'home.html'
    def get(self, request):
        return render(request, self.template_name)



class About(View):
    template_name = 'about.html'
    def get(self, request):
        return render(request, self.template_name)


class Services(View):
    template_name = 'services.html'
    def get(self, request):
        return render(request, self.template_name)


class Contact(View):
    template_name = 'contact.html'
    def get(self, request):
        return render(request, self.template_name)