from django.shortcuts import render

from .models import Make, Model, Vehicle, FuelUp

# Create your views here.

def index(request):
  context = {'vehicles':Vehicle.objects.all()}
  return render(request, 'mpg/index.html', context)
