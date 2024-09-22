# api/urls.py

from django.urls import path
from myapp.views import admin

urlpatterns = [
    path('admin/', admin),
    # Add your other URL patterns here
]