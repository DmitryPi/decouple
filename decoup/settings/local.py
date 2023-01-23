from .base import *  # noqa
from .base import env

DEBUG = True
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="cZwrG7UEpaTy7XXYlNwfKgrBxgXTUP6BS9zCSSfk4LiX6IL7cwdHZNkAQdoq2JMm",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa F405
