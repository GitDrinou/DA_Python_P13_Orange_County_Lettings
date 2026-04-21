"""
URL configuration for the profiles application.
This module defines the routes used to access the profiles index page
and individual profile detail pages.
"""

from django.urls import path
from . import views


app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile_detail, name='profile'),
]
