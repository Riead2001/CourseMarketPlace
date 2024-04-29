from django.shortcuts import render
from courses.models import Course
from django.views.generic import ListView

'''
def home(request):
    courses = Course.objects.all()
    return render(request, 'courses/home.html', {'courses': courses})
'''


from django.db.models import Avg
from courses.models import Rating

class Home(ListView):
    template_name = 'courses/home.html'
    queryset = Course.objects.filter(active=True)
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Calculate the average rating for each course
        for course in context['courses']:
            avg_rating = Rating.objects.filter(coursename=course.name).aggregate(Avg('rating'))['rating__avg']
            course.avg_rating = avg_rating
        
        return context
