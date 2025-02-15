from django.contrib import admin
from django.urls import path, include, re_path
from core.views import view_home, view_home_tag_retirada_sp, view_home_tag_coleta_sp, view_home_tag_transporte_sp, view_home_tag_zona_sul, view_home_tag_retiradas_sp
from core.sitemaps import sitemap
from core.robots import robots 

urlpatterns = [
    path('', view_home),
    path('retirada-de-entulho-sao-paulo/', view_home_tag_retiradas_sp),
    path('tag/retirada-de-entulho-em-sao-paulo/', view_home_tag_retirada_sp),
    path('tag/transporte-de-entulho-em-sao-paulo/', view_home_tag_transporte_sp),
    path('tag/coleta-de-entulho-em-sao-paulo/', view_home_tag_coleta_sp),
    path('tag/retirada-de-entulho-zona-sul/', view_home_tag_zona_sul),
    path('sitemap.xml', sitemap, name='sitemap'),
    re_path(r'^robots\.txt', robots), 
]
