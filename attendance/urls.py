# attendance/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('upload/success/', upload_success, name='upload_success'),  # Add this line
]
# attendance/views.py
from django.shortcuts import render



