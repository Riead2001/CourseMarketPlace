
# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Payment
from courses.forms import PaymentForm


def payment_success(request):
    return render(request, 'payment_success.html')