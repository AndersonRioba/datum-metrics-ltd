import os
import sys

# Add project directory to sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

# Set production settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datum_metrics.settings.production")

# MySQL driver hook
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

# Expose WSGI application for Phusion Passenger / LiteSpeed
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
