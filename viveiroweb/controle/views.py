from django.shortcuts import render
from .models import Planta

# Create your views here.

def home(request):
    plantas_aleatorias = Planta.objects.order_by('?')[:3]
    return render(request, 'home.html', {'plantas': plantas_aleatorias})
