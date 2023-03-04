from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sales_orders(request):
    return HttpResponse("Sales Orders")

def purchase_orders(request):
    return HttpResponse("Purchase Orders")