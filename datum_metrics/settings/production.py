from .base import *

DEBUG = False

ALLOWED_HOSTS = ['datum-metrics.com', 'www.datum-metrics.com']

# Use a strong secret key - generate one with:
# python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
SECRET_KEY = 'qkjfoldb5bb9bc#0no#^wvm98$xcgrp+yq!e4)4pk=rg@9(*kt'

# Production database (cPanel MySQL)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "raveyhpw_datum-metrics",   # cPanel DB name format
        "USER": "raveyhpw_datum-metrics",           # cPanel DB user format
        "PASSWORD": "K?wAQ7N2qFiA^g2e",
        "HOST": "localhost",
        "PORT": "3306",
        "OPTIONS": {
            "charset": "utf8mb4",
            "init_command": "SET NAMES utf8mb4 COLLATE utf8mb4_general_ci;",
        },
    }
}

# Static files served by the web server
STATIC_ROOT = BASE_DIR / 'public' / 'static'
STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR / 'public' / 'media'
MEDIA_URL = '/media/'

# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
