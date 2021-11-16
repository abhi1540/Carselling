from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class Login(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, **kwargs):
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You Are Now Logged In:")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Login Credentials")
            return redirect('login')




class Registration(View):
    template_name = 'register.html'

    def get(self, request):
        print(request.method)
        return render(request, self.template_name)

    def post(self, request, **kwargs):

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']


        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User Already Exists")
                return redirect('registration')

            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email ID Already Used")
                    return redirect('registration')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, "You Are Successfully Logged In: ")
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, "Yo Are Successfully Registered..")
                    return redirect('login')
        else:
            messages.error(request, "Password Doesn't Match")
            return redirect('registration')


class Logout(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, **kwargs):

        auth.logout(request)
        # messages.success(request, "You Are Successfully Logged Out")
        return redirect('home')

# @login_required( login_url='login')
class Dashboard(LoginRequiredMixin, View ):
    template_name = 'dashboard.html'
    login_url = 'login'

    def get(self, request):

        user_inquiry = Contact.objects.order_by('-created_date').filter(user_id=request.user.id)
        data = {
            'user_inquiry': user_inquiry
        }
        return render(request, self.template_name, data)