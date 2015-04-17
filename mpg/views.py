from django.shortcuts import get_object_or_404,render

from .models import Make, Model, Vehicle, FuelUp

# Create your views here.

def index(request):
  context = {'makes':Make.objects.all()}
  return render(request, 'mpg/index.html', context)


def model(request, model_name):
  model = Model.objects.get(name__exact=model_name)
  context = {'model':model}
  return render(request, 'mpg/model.html', context)


def make(request, make_name):
  make = Make.objects.get(name__exact=make_name)
  context = {'make':make}
  return render(request, 'mpg/make.html', context)


def vehicle(request, vehicle_id):
  vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
  context = {'vehicle':vehicle}
  return render(request, 'mpg/vehicle.html', context)
