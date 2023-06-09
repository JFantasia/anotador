from django.shortcuts import render

def home(request):
    data = {
        "titulo": "VISTA"
    }
    return render(request, "home.html", data)

def buscar(request):
    data = {
        "titulo": "VISTA"
    }
    return render(request, "buscar.html", data)
