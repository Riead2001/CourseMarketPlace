from django.shortcuts import render, redirect
from django.contrib import messages


from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import course, UserCourse, Course, user_course,Scholarship


def ScholarshipView(request, slug):
    # Retrieve the course object based on the slug
    course = Course.objects.get(slug=slug)
    if request.method == 'POST':
        reason = request.POST.get('reason')
        description = request.POST.get('description')
        # Get the currently logged-in user
        user = request.user
        # Create a new Rating instance with the provided data
        scholarship_instance = Scholarship.objects.create(
            username=user,
            coursename=course.name,
            reason=reason,
            description = description,
        )
        # Save the rating instance to the database
        scholarship_instance.save()
        # Redirect the user back to the rating page for the current course
        return redirect('coursepage', slug=slug)
    
    
    
    return render(request, 'courses/scholarship.html', {'course': course})