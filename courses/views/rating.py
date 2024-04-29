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

def Rating_View(request, slug):
    # Retrieve the course object based on the slug
    course = Course.objects.get(slug=slug)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        review = request.POST.get('review')
        # Get the currently logged-in user
        user = request.user
        # Create a new Rating instance with the provided data
        rating_instance = Rating.objects.create(
            username=user,
            coursename=course.name,
            rating=rating,
            review=review
        )
        # Save the rating instance to the database
        rating_instance.save()
        # Redirect the user back to the rating page for the current course
        return redirect('course_rating', slug=slug)

    # Filter ratings based on the coursename
    ratings = Rating.objects.filter(coursename=course.name)
    # Calculate the average rating of the course
    avg_rating = ratings.aggregate(Avg('rating'))['rating__avg']
    print(avg_rating)
    # Retrieve the last 5 reviews
    last_reviews = ratings.order_by('-username')[:5]
    print(last_reviews)
    
    return render(request, 'courses/rating.html', {'ratings': ratings, 'avg_rating': avg_rating, 'last_reviews': last_reviews})




    