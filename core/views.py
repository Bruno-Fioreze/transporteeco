from django.shortcuts import render


def view_home(request):
    return render(request, 'home.html')

def view_home_teste(request):
    return render(request, 'faq.html')
