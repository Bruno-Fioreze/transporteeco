from django.contrib import admin
from django.urls import path, include
from core.views import view_home


urlpatterns = [
    path('', view_home),
]
