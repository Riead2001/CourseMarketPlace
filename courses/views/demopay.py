from django.shortcuts import render
from django.http import HttpResponse
from courses.models.demopay import DemoPay

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models.course import Course
from courses.models.demopay import DemoPay
from courses.models.user_course import UserCourse



@login_required
def Demopay(request, slug):
    
    try:
        course = Course.objects.get(slug=slug)
        if request.method == 'POST':
            
           
            user = request.user
            # Create a new Rating instance with the provided data
            payment_done= DemoPay.objects.create(
                user=user,
                course_name=course.name,
                
            )
            payment_done.save()
            course_added= UserCourse.objects.create(
                user=user,
                course=course,
                
            )
            
           
            
            course_added.save()
            
            return redirect('demopay', slug=slug)
    except Course.DoesNotExist:
        
        messages.error(request, 'Course not found.')
        return redirect('home') 
    
    context = {
        'course': course
    }
    return render(request, 'courses/demopay.html', context)
