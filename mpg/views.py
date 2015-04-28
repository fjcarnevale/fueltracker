from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.core.urlresolvers import reverse

from .models import Make, Model, Vehicle, FuelUp

# Create your views here.

def get_user(request):
  if request.user.is_authenticated():
    user = request.user
  else:
    user = None
  return user
    
def login_user(request):
  username = request.POST['username']
  password = request.POST['password']

  user = authenticate(username=username, password=password)

  if user is not None:
    if user.is_active:
      login(request, user)

  return HttpResponseRedirect(reverse('index'))
  
def logout_user(request):
    logout(request)
    
    return HttpResponseRedirect(reverse('index'))


def register(request):
  username = request.POST['username']
  email = request.POST['email']
  password = request.POST['password']

  user = User.objects.create_user(username, email, password)
  user = authenticate(username=username, password=password)

  if user is not None:
    if user.is_active:
      login(request, user)

  return HttpResponseRedirect(reverse('index'))

def register_page(request):
  return render(request, 'mpg/register.html')

def index(request):
  user = get_user(request)
  context = {'user':user, 'makes':Make.objects.all()}
  return render(request, 'mpg/index.html', context)


def model(request, model_name):
  user = get_user(request)
  model = Model.objects.get(name__exact=model_name)
  context = {'user':user, 'model':model}
  return render(request, 'mpg/model.html', context)


def make(request, make_name):
  user = get_user(request)
  make = Make.objects.get(name__exact=make_name)
  context = {'user':user, 'make':make}
  return render(request, 'mpg/make.html', context)


def vehicle(request, vehicle_id):
  user = get_user(request)
  vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
  context = {'user':user,'vehicle':vehicle}
  return render(request, 'mpg/vehicle.html', context)

def addMake(request):
  make_name = request.POST['make']
  
  if not len(Make.objects.filter(name=make_name)):
    make = Make()
    make.name = make_name
    make.save()
    
  
