"""
URL configuration for the lettings application
This module defines the routes used to access the lettings index page and
the detail page for each lettings.
"""

from django.urls import path
from . import views


app_name = "lettings"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting_detail, name='letting'),
]
