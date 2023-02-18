from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):    
    return render(request, 'projetos/index.html')

def page(request):
    return render(request, 'projetos/page.html')

