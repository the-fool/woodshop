from django.shortcuts import redirect, render
from gems.models import Gem
from django.template.context_processors import request

def home_page(request):
    return render(request, 'home.html')

def view_gems(request):
    return render(request, 'home.html')
