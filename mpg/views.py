from django.shortcuts import render

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
