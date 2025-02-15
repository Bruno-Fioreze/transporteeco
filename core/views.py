from django.shortcuts import render


def view_home(request):
    return render(request, 'home.html')

def view_home_teste(request):
    return render(request, 'faq.html')

def view_home_tag(request): 
    context = {"type": "retirada", "title": "RETIRADA", "regiao": "São Paulo"}
    return render(request, "tag.html", context=context)

def view_home_tag_retirada_sp(request): 
    context = {"type": "retirada", "title": "RETIRADA", "regiao": "São Paulo"}
    return render(request, "tag.html", context=context)

def view_home_tag_retiradas_sp(request): 
    context = {"type": "retiradas", "title": "RETIRADAS", "regiao": "São Paulo"}
    return render(request, "tag.html", context=context)

def view_home_tag_coleta_sp(request): 
    context = {"type": "coleta", "title": "COLETA", "regiao": "São Paulo"}
    return render(request, "tag.html", context=context)

def view_home_tag_transporte_sp(request): 
    context = {"type": "transporte", "title": "Transporte", "regiao": "São Paulo"}
    return render(request, "tag.html", context=context)


def view_home_tag_zona_sul(request): 
    context = {"type": "retirada", "title": "Retirada", "regiao": "Zona Sul"}
    return render(request, "tagV2.html", context=context)