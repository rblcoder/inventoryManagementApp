from django.contrib import admin
from django.apps import apps

# Register your models here.

products_models = apps.get_app_config('products').get_models()

for model in products_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

admin.site.site_header = "Inventory Management System"
