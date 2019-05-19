from django.shortcuts import render
from app.forms import CadastroForm
from app import views

# Create your views here.

def index(request):
    return render(request, 'index.html')

def fazer_cadastro(request):
    formulario = CadastroForm(request.POST or None)
    msg = ''
    if formulario.is_valid():
        formulario.save()
        formulario = CadastroForm()
        
    contexto = {
        'form' : formulario,
    }

    return render(request, 'cadastro.html', contexto)