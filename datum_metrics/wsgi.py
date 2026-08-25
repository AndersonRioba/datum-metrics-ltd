"""
WSGI config for datum_metrics project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os
import pymysql

pymysql.install_as_MySQLdb()


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datum_metrics.settings.dev")

application = get_wsgi_application()
