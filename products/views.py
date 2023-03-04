import datetime
import logging

from django.shortcuts import render

from .models import Currency, Category

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    # return HttpResponse("Hello, world. You are in products index")
    return render(request, 'products/index.html', {})


def categories(request):
    logger.info("Categories was accessed at " + str(datetime.datetime.now()) + ' hours!')
    categories_list = Category.objects
    context = {
        'categories_list': categories_list
    }
    return render(request, 'products/categories.html', context)


def currencies(request):
    logger.info("Currencies was accessed at " + str(datetime.datetime.now()) + ' hours!')
    currencies_list = Currency.objects
    context = {
        'currencies_list': currencies_list,
    }
    return render(request, 'products/currencies.html', context)


def dashboard(request):
    return render(request, 'products/dashboard.html', {})
