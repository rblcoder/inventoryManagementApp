from django.contrib import admin
from django.apps import apps

# Register your models here.

orders_models = apps.get_app_config('orders').get_models()

for model in orders_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
