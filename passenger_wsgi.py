import os
import sys

# Add project directory to sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

# Force production settings BEFORE any Django imports so that
# datum_metrics/__init__.py correctly skips the XAMPP-only DB patches.
# Using direct assignment (not setdefault) so this can never be overridden
# by a missing or mis-scoped env var from LiteSpeed/Passenger.
os.environ["DJANGO_SETTINGS_MODULE"] = "datum_metrics.settings.production"

# MySQL driver hook
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

# Expose WSGI application for Phusion Passenger / LiteSpeed
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
