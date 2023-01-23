from .base import *  # noqa
from .base import env

DEBUG = True
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="cZwrG7UEpaTy7XXYlNwfKgrBxgXTUP6BS9zCSSfk4LiX6IL7cwdHZNkAQdoq2JMm",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
