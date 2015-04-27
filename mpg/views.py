from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.core.urlresolvers import reverse

from .models import Make, Model, Vehicle, FuelUp

# Create your views here.

def index(request):
  if request.user.is_authenticated():
    user = request.user
  else:
    user = None

  context = {'user':user, 'makes':Make.objects.all()}
  return render(request, 'mpg/index.html', context)

def login_user(request):
  username = request.POST['username']
  password = request.POST['password']

  user = authenticate(username=username, password=password)

  if user is not None:
    if user.is_active:
      login(request, user)  

  return HttpResponseRedirect(reverse('index'))


def register(request):
  username = request.POST['username']
  email = request.POST['email']
  password = request.POST['password']

  user = User.objects.create_user(username, email, password)

  if user is not None:
    if user.is_active:
      login(request, user)

  return HttpResponseRedirect(reverse('index'))

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

def addMake(request):
  make_name = request.POST['make']
  
  if not len(Make.objects.filter(name=make_name)):
    make = Make()
    make.name = make_name
    make.save()
    
  
