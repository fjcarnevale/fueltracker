from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.core.urlresolvers import reverse

from .models import Make, Model, Vehicle, FuelUp

# Create your views here.

# Convenience function to get the current user
def get_user(request):
  # Check if user is authenticated
  if request.user.is_authenticated():
    # if so, return the user
    user = request.user
  else:
    # otherwise, return None
    user = None
    
  return user
  
# View to handle user authentication
def login_user(request):
  # get username and password
  username = request.POST['username']
  password = request.POST['password']

  # authenticate the user
  user = authenticate(username=username, password=password)

  # check that user was authenticated properly
  if user is not None:
    if user.is_active:
      # if so, log them in
      login(request, user)

  # TODO handle authentication errors

  # redirect to the index
  return HttpResponseRedirect(reverse('index'))
  
# View to handle logging out users
def logout_user(request):
  # logout the user
  logout(request)
  
  # redirect to the index
  return HttpResponseRedirect(reverse('index'))

# Simple view to show the register page
def register_page(request):
  return render(request, 'mpg/register.html')

# View to handle registering users
def register(request):
  # Get the user information
  username = request.POST['username']
  email = request.POST['email']
  password = request.POST['password']

  # Create and authenticate the user
  user = User.objects.create_user(username, email, password)
  user = authenticate(username=username, password=password)

  # Check that user was authenticated properly
  if user is not None:
    if user.is_active:
      # if so, log them in
      login(request, user)

  # redirect to the index
  return HttpResponseRedirect(reverse('index'))

# Index view
def index(request):
  # Get the user
  user = get_user(request)
  
  # Set the context, retrieving all makes
  context = {'user':user, 'makes':Make.objects.all()}
  return render(request, 'mpg/index.html', context)

# Make view
def make(request, make_name):
  # get the user
  user = get_user(request)
  
  # get the make by name
  make = Make.objects.get(name__exact=make_name)
  
  # set the context and render the page
  context = {'user':user, 'make':make}
  return render(request, 'mpg/make.html', context)


# Model view
def model(request, model_name):
  # Get the user
  user = get_user(request)
  
  # Get the model based on the name
  model = Model.objects.get(name__exact=model_name)
  
  # Set the context and render the page
  context = {'user':user, 'model':model}
  return render(request, 'mpg/model.html', context)


# Vehicle view
def vehicle(request, vehicle_id):
  # get the user
  user = get_user(request)
  
  # get the vehicle by ID or 404
  vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
  
  # set the context and render the page
  context = {'user':user,'vehicle':vehicle}
  return render(request, 'mpg/vehicle.html', context)

# View to add a new make
# TODO this will become part of the API
def addMake(request):
  # get the name of the new make
  make_name = request.POST['make']
  
  # if a make does not already exist by that name
  if not len(Make.objects.filter(name=make_name)):
    # create and save the new make
    make = Make()
    make.name = make_name
    make.save()
    
  
