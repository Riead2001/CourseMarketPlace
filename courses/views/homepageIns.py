from django.shortcuts import render
from courses.models import Course
from django.views.generic import ListView

'''
def home(request):
    courses = Course.objects.all()
    return render(request, 'courses/home.html', {'courses': courses})
'''


class Home1(ListView):
    template_name = 'courses/home1.html'
    queryset = Course.objects.filter(active=True)
    context_object_name = 'courses'