from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from courses.models import Course, Payment, UserCourse
from courses.templatetags.course_custom_tag import apply_discount
from django.contrib.auth.decorators import login_required
from time import time
from Project.settings import KEY_ID, KEY_SECRET
import razorpay





client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def bank_login(request):
    if request.method == 'POST':
        bank_id = request.POST.get('bank_id')
        password = request.POST.get('password')
        user = authenticate(request, username=bank_id, password=password)
        if user is not None:
            login(request, user)
            return redirect('checkout', slug=course.slug)  # Redirect to the checkout page after successful login
        else:
            error = "Invalid bank ID or password. Please try again."
            return render(request, 'courses/bank_login.html', {'error': error})
    else:
        return render(request, 'courses/bank_login.html')



@login_required(login_url='login')
def checkout(request, slug):
    
    return render(request, 'courses/checkout.html', context=context)







@csrf_exempt
def verify_payment(request):


    if request.method == 'GET':
        return HttpResponse('Sorry, Something went wrong!')


    data = request.POST

    try:
        params_dict = {
            'razorpay_order_id': data['razorpay_order_id'],
            'razorpay_payment_id': data['razorpay_payment_id'],
            'razorpay_signature': data['razorpay_signature']
        }
        client.utility.verify_payment_signature(params_dict)


        payment = Payment.objects.get(order_id=data.get('razorpay_order_id'))
        payment.payment_id = data.get('razorpay_payment_id')
        payment.status = True


        user_course = UserCourse()
        user_course.user = request.user
        user_course.course = payment.course
        user_course.save()


        

        payment.user_course = user_course
        payment.save()



    except:
        return HttpResponse('Payment Faild')



    return redirect('my_courses')