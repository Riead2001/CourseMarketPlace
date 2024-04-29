from django.shortcuts import render, redirect
from courses.models import Course, Video, Quiz
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


def Cc(request):
    if request.method == 'POST':
        # Course Information
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        description = request.POST.get('description')
        price = request.POST.get('price')
        discount = request.POST.get('discount', 0)
        length = request.POST.get('length')
        image = request.FILES.get('image')
        resource = request.FILES.get('resource')
        
        # Create the course object
        course = Course.objects.create(
            name=name,
            slug=slug,
            description=description,
            price=price,
            discount=discount,
            length=length,
            image=image,
            resource=resource
        )

        # Video Information
        video_serial_numbers = request.POST.getlist('video_serial_number')
        video_titles = request.POST.getlist('video_title')
        video_ids = request.POST.getlist('video_id')
        is_previews = request.POST.getlist('is_preview')

        # Loop through each video and create Video objects
        for serial_number, title, video_id, is_preview in zip(video_serial_numbers, video_titles, video_ids, is_previews):
            # Convert is_preview to boolean
            is_preview = is_preview.lower() == 'on'

            # Create the Video object
            Video.objects.create(
                course=course,
                serial_number=serial_number,
                title=title,
                video_id=video_id,
                is_preview=is_preview
            )

        # Quiz Information
        quiz_numbers = request.POST.getlist('quiz_number')
        quiz_links = request.POST.getlist('quiz_link')

        # Loop through each quiz and create Quiz objects
        for quiz_number, quiz_link in zip(quiz_numbers, quiz_links):
            # Create the Quiz object
            Quiz.objects.create(
                course_name=course.name,
                quiz_number=quiz_number,
                quiz_link=quiz_link
            )

        # Redirect to a success page or wherever appropriate
        return redirect('homepageIns')  # Change 'login' to the desired URL

    return render(request, 'courses/cc.html')