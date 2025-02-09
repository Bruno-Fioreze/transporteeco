from django.contrib import admin
from django.urls import path, include, re_path
from core.views import view_home, view_home_teste
from core.sitemaps import sitemap
from core.robots import robots 

urlpatterns = [
    path('', view_home),
    path('retirada-entulho-sao-paulo', view_home),
    path('retirada-entulho-sao-paulo/', view_home_teste),
    path('transporte-entulho-sao-paulo', view_home_teste),
    path('coleta-entulho-sao-paulo', view_home_teste),
    path('coleta-entulho-sp', view_home_teste),
    path('transporte-entulho-sp', view_home_teste),
    path('retirada-entulho-sp', view_home_teste),
    path('retira-entulho-sp', view_home_teste),
    path('retira-entulho-sao-paulo', view_home_teste),
    path('sitemap.xml', sitemap, name='sitemap'),
    re_path(r'^robots\.txt', robots),
    path('retira-entulho-sao-paulo/sitemap.xml', sitemap),
    path('retira-entulho-sp/sitemap.xml', sitemap),
    path('retirada-entulho-sp/sitemap.xml', sitemap),
    path('transporte-entulho-sp/sitemap.xml', sitemap),
    path('coleta-entulho-sp/sitemap.xml', sitemap),
    path('coleta-entulho-sao-paulo/sitemap.xml', sitemap),
    path('transporte-entulho-sao-paulo/sitemap.xml', sitemap),
    path('retirada-entulho-sao-paulo/sitemap.xml', sitemap),

]
