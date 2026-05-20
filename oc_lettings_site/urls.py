"""
Root URL configuration for the OC Lettings Site project.
This module routes requests to the main home page and delegates
sub-routes to the lettings and profiles applications.
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('test-500/', views.trigger_error, name='500'),
    path('admin/', admin.site.urls),
]
