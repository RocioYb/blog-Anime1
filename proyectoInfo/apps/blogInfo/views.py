from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactoForm

# Create your views here.

def home(request):
   # return HttpResponse("Bienvenido a la pagina principal")
    return render(request, 'index.html')

def post(request):
    return render(request, 'post.html')

def Categorias(request):
    return render(request, 'categoria.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Aquí se puede procesar los datos del formulario
            datos = form.cleaned_data
            print(datos)
            return redirect('home')  # Redirige a la página principal después de enviar el formulario
    else:
        form = ContactoForm()
    
    return render(request, 'contacto.html', {'form': form})
