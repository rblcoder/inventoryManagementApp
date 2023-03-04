from django.urls import path

from . import views
app_name = 'orders'
urlpatterns = [
    path('sales', views.sales_orders, name='sales_orders'),
    path('purchase', views.purchase_orders, name='purchase_orders'),
]