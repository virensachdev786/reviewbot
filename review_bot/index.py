from django.http import HttpResponse
from django.shortcuts import render

def checkout(request):
    return render(request, 'checkout.html')

def landing(request):
    return render(request, 'landing.html')

def pricing(request):
    return render(request, 'pricing.html')