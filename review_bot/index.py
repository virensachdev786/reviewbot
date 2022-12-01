from django.http import HttpResponse
from django.shortcuts import render

def checkout(request):
    return render(request, 'checkout.html')

def landing(request):
    return render(request, 'landing.html')

def pricing(request):
    return render(request, 'pricing.html')

def confirm(request):
    return render(request, 'confirm.html')

def existingbusinesses(request):
    return render(request, 'existingbusinesses.html')

def newbusiness(request):
    return render(request, 'newbusiness.html')

def test(request):
    return render(request, 'test.html')
