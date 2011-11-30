from django.conf.global_settings import *
import os


STATIC_ROOT = MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
STATIC_URL = MEDIA_URL = "/media/"
INSTALLED_APPS = (
    "cssreload",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'cssreload.middleware.CSSReloadMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

DEBUG = True
