from django.shortcuts import HttpResponse
from django.contrib import admin
from django.urls import path
from courses.views import coursePage, LoginView, SignupView, Home, logout_view, checkout, verify_payment, MyCoursesList,Home1,About,Update, Discussion, Demopay , Cc
from . import views
from courses.views.rating import Rating_View
from courses.views.scholarshipView import ScholarshipView
def index(request):
    return HttpResponse('i get it')

urlpatterns = [
    path('', Home.as_view(), name='homepage'),
    path('Ins/', Home1.as_view(), name='homepageIns'),
    path('course/<str:slug>/', coursePage, name='coursepage'),
    path('login/', LoginView.as_view(), name='login'),
    path('checkout/<str:slug>/', checkout, name="checkout"),
    path('verify_payment/', verify_payment, name="verify_payment"),
    path('my-courses/', MyCoursesList.as_view(), name='my_courses'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
    path('about/', About, name='about'),
    path('update/', Update, name='update'),
    path('course/<str:slug>/rating/', Rating_View, name='course_rating'),
    path('course/<str:slug>/scholarship/', ScholarshipView, name='scholarship'),
    path('course/<str:slug>/discussion/', Discussion, name='discussion'),
    path('course/<str:slug>/demopay/', Demopay, name='demopay'),
    path('Ins/cc/', Cc, name='cc'),
    
   
   
]
