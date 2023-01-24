from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["decoup.ru"])
STATIC_ROOT = env("STATIC_ROOT")

# SECURITY
# ------------------------------------------------------------------------------
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
