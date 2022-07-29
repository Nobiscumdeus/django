"""
WSGI config for websiteapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websiteapp.settings')
#Note initially from dj_static import Cling wasn't here. It bascially for static files 
from dj_static import Cling
#Initially this was application=get_wsgi_application()
application = Cling(get_wsgi_application())
