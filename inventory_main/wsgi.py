"""
WSGI config for inventory_main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from settings import base

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_main.settings')
if base.DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_main.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_main.settings.production')

application = get_wsgi_application()
