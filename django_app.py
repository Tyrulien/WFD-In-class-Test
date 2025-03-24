# django_app.py
import sys
from django.conf import settings
from django.urls import path
from django.http import HttpResponse
from django.core.management import execute_from_command_line

DEBUG = True

if not settings.configured:
    settings.configure(
        DEBUG=DEBUG,
        SECRET_KEY='a-very-secret-key',
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=['*'],
        MIDDLEWARE=[
            'django.middleware.common.CommonMiddleware',
        ],
        INSTALLED_APPS=(
            'django.contrib.contenttypes',
            'django.contrib.staticfiles',
        ),
        STATIC_URL='/static/',  # Added STATIC_URL setting
    )

def index(request):
    return HttpResponse("Status: Working")

urlpatterns = [
    path('', index),
]

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
