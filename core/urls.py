from django.contrib import admin
from django.urls import path, include
from core.views import view_home


urlpatterns = [
    path('', view_home),
    path('retirada-entulho-sao-paulo', view_home),
    path('transporte-entulho-sao-paulo', view_home),
    path('coleta-entulho-sao-paulo', view_home),
    path('coleta-entulho-sp', view_home),
    path('transporte-entulho-sp', view_home),
    path('retirada-entulho-sp', view_home),
    path('retira-entulho-sp', view_home),
    path('retira-entulho-sao-paulo', view_home),
]
