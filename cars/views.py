from django.shortcuts import render
from django.views import View
# Create your views here.
class Cars(View):
    template_name = 'cars.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

