from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello, world. You are in products index")
    return render(request, 'products/index.html', {})

def categories(request):
    # return HttpResponse("Hello, world. You are in products index")
    return render(request, 'products/categories.html', {})

def currencies(request):
    # return HttpResponse("Hello, world. You are in products index")
    return render(request, 'products/currencies.html', {})

def dashboard(request):
    # return HttpResponse("Hello, world. You are in products index")
    return render(request, 'products/dashboard.html', {})
