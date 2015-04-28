from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Class for MPG Users
class MpgUser(models.Model):
  user = models.ForeignKey(User)
  
  def __str__(self):
    return self.user.username

# Class for Makes of vehicles
class Make(models.Model):
  name = models.CharField(max_length=20)

  def __str__(self):
    return self.name

# Class for Models of vehicles
class Model(models.Model):
  make = models.ForeignKey(Make)
  name = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  # Calculates the average MPG for all vehicles of this model
  def average_mpg(self):
    # get all the vehicles of this model
    vehicles = self.vehicle_set.all()
    
    # gather all the fuel ups
    fuel_ups = []
    for vehicle in vehicles:
      fuel_ups.extend(vehicle.fuelup_set.all())

    # if no fuel ups, return 0
    if not fuel_ups:
      return 0

    # calculate and return the average MPG
    return sum([fu.miles for fu in fuel_ups]) / sum([fu.gallons for fu in fuel_ups])

# Class for Vehicles
class Vehicle(models.Model):
  owner = models.ForeignKey(MpgUser)
  model = models.ForeignKey(Model)
  year = models.IntegerField()
  name = models.CharField(max_length=20)

  def __str__(self):
    return self.name

# Class for FuelUps
class FuelUp(models.Model):
  date = models.DateField()
  miles = models.IntegerField(default = 0)
  gallons = models.FloatField()
  cost = models.FloatField()
  vehicle = models.ForeignKey(Vehicle)

  def __str__(self):
    return "%.2f gal at $%.2f: %.1f MPG" % (self.gallons, self.cost, self.miles / self.gallons)

  def mpg(self):
    return self.miles / self.gallons
