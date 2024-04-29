from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from courses.forms import RegistrationForm as UserCreationForm
from courses.forms import LoginForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.views.generic.edit import FormView
from django.shortcuts import render

from django.contrib.auth import login, get_user_model 
from django.contrib.auth.models import User
from django.views.generic import FormView
from courses.forms import RegistrationForm
from django.urls import reverse_lazy

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate  # Add this import
from django.contrib.auth import get_user_model

class SignupView(FormView):
    template_name = 'courses/signup.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




'''
class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'courses/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            user = form.save()
            if (user is not None):
                return redirect('login')
        return render(request, 'courses/signup.html', {'form': form})
'''




class LoginView(FormView):
    template_name = 'courses/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        # Login the user
        login(self.request, form.cleaned_data['user'])

        # Redirect based on role
        role = form.cleaned_data.get('role')
        if role == 'student':
            return redirect('homepage')  # Redirect to the homepage for students
        elif role == 'instructor':
            return redirect('homepageIns')  # Redirect to the homepage for instructors
        else:
            # Handle invalid role (optional)
            return super().form_valid(form)

'''
class LoginView(View):
    next_url = None
    def get(self, request):
        LoginView.next_url = request.GET.get('next')

        if (request.user.is_authenticated):
            return redirect('homepage')

        form = LoginForm()
        return render(request, 'courses/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request, request.POST)
        if (form.is_valid()):

            if (request.user.is_authenticated):

                if LoginView.next_url:
                    return HttpResponseRedirect(LoginView.next_url)

                return redirect('homepage')

        return render(request, 'courses/login.html', {'form': form})
'''

def logout_view(request):
    logout(request)
    return redirect('homepage')
