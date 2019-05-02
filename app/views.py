from django.shortcuts import render
from app import views

# Create your views here.

def index(request):
    return render(request, 'index.html')