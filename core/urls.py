from django.contrib import admin
from django.urls import path, include
from core.views import view_home
from core.sitemaps import sitemap
from core.robots import robots 

urlpatterns = [
    path('', view_home),
    path('retirada-entulho-sao-paulo', view_home),
    path('retirada-entulho-sao-paulo/', view_home),
    path('transporte-entulho-sao-paulo', view_home),
    path('coleta-entulho-sao-paulo', view_home),
    path('coleta-entulho-sp', view_home),
    path('transporte-entulho-sp', view_home),
    path('retirada-entulho-sp', view_home),
    path('retira-entulho-sp', view_home),
    path('retira-entulho-sao-paulo', view_home),
    path('sitemap.xml', sitemap, name='sitemap'),
    path('robots.txt', robots, name="robots"),
    path('robots.txt/', robots, name="robots2"),
    path('retira-entulho-sao-paulo/sitemap.xml', sitemap),
    path('retira-entulho-sp/sitemap.xml', sitemap),
    path('retirada-entulho-sp/sitemap.xml', sitemap),
    path('transporte-entulho-sp/sitemap.xml', sitemap),
    path('coleta-entulho-sp/sitemap.xml', sitemap),
    path('coleta-entulho-sao-paulo/sitemap.xml', sitemap),
    path('transporte-entulho-sao-paulo/sitemap.xml', sitemap),
    path('retirada-entulho-sao-paulo/sitemap.xml', sitemap),

]
