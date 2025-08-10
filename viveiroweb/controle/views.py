<<<<<<< HEAD
from django.shortcuts import render #, get_list_or_404 
#from django.contrib.auth.decorators import login_required // isso vai dizer que a rota só pode ser acessada por usuários logados

# Create your views here.


=======
from django.shortcuts import render
from .models import Planta

# Create your views here.

def home(request):
    plantas_aleatorias = Planta.objects.order_by('?')[:3]
    return render(request, 'home.html', {'plantas': plantas_aleatorias})
>>>>>>> 356b4385df98553941776a19c61ca86af5705e4e
