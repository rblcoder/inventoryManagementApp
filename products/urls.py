from django.urls import path

from . import views
app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('categories', views.categories, name='categories'),
    path('currencies', views.currencies, name='currencies'),
    path('dashboard', views.dashboard, name='dashboard'),
]