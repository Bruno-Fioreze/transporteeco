# views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import os

def  robots(request):
    sitemap_path = os.path.join(settings.BASE_DIR, 'static', 'robots.txt')
    try:
        with open(sitemap_path, 'r') as file:
            sitemap_content = file.read()
        return HttpResponse(sitemap_content, content_type="text/plain")
    except FileNotFoundError:
        return HttpResponse(status=404)