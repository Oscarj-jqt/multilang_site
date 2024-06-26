"""
WSGI config for multilang_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import sys

# Ajoutez le chemin du projet au PYTHONPATH
# sys.path.append('/opt/render/project/src')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.multilang_site.settings')

application = get_wsgi_application()