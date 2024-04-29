from django.shortcuts import render
from courses.models.rating import Rating
from django.shortcuts import render, HttpResponse, redirect
from courses.models import course, UserCourse, Course, user_course
from courses.models.video import Video
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

# views.py
from django.shortcuts import redirect

from django.db.models import Avg

def Discussion(request, slug):
    # Retrieve the course object based on the slug
    course = Course.objects.get(slug=slug)
    coursename = course.name
    
    
    return render(request, 'courses/discussion.html')




    