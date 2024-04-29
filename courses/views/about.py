from django.shortcuts import render
from courses.models.customuser import CustomUser

def About(request):
    # Retrieve user data from CustomUser model
    user = CustomUser.objects.get(username=request.user.username)

    # Pass user data to the template
    context = {'user': user}
    
    # Render the HTML template with user data
    return render(request, 'courses/about.html', context)

