# views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import os

def sitemap(request):
    sitemap_path = os.path.join(settings.BASE_DIR, 'static', 'sitemap.xml')
    print(
        sitemap_path
    )
    try:
        with open(sitemap_path, 'r') as file:
            sitemap_content = file.read()
        return HttpResponse(sitemap_content, content_type="application/xml")
    except FileNotFoundError:
        return HttpResponse(status=404)