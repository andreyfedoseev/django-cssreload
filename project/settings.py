from django.conf.global_settings import *
import os


MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
STATIC_URL = "/static/"


INSTALLED_APPS = (
    "django.contrib.staticfiles",
    "django.contrib.markup",
    "cssreload",
    "project",
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'cssreload.middleware.CSSReloadMiddleware',
)

DEBUG = True


ROOT_URLCONF = "project.urls"
