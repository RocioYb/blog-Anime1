from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
   # return HttpResponse("Bienvenido a la pagina principal")
    return render(request, 'index.html')

def post(request):
    return render(request, 'post.html')

def Categorias(request):
    return render(request, 'categoria.html')

def contacto(request):
    return render(request, 'contacto.html')
