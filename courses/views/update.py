from django.shortcuts import render, redirect
from courses.models.customuser import CustomUser

def Update(request):
    if request.method == 'POST':
        # Retrieve form data
        dob = request.POST.get('dob')
        education = request.POST.get('education')
        college = request.POST.get('college')
        skills = request.POST.get('skills')
        
        # Retrieve the current user
        user = CustomUser.objects.get(username=request.user.username)
        
        # Update user data
        user.date_of_birth = dob
        user.education = education
        user.college_name = college
        user.skills = skills
        
        # Save changes to the database
        user.save()
        
        # Redirect to a relevant page
        return redirect('about')  # Assuming 'about' is the name of the view for the user's profile
        
    else:
        # If not a POST request, render the update form
        return render(request, 'courses/update.html')
