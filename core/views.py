from django.shortcuts import render


def view_home(request):
    print("chegou aqui my broooo")
    return render(request, 'home.html')