from django.db import models

# Create your models here.

class Make(models.Model):
  name = models.CharField(max_length=20)

  def __str__(self):
    return self.name

class Model(models.Model):
  make = models.ForeignKey(Make)
  name = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def average_mpg(self):
    vehicles = self.vehicle_set.all()
    
    fuel_ups = []
    for vehicle in vehicles:
      fuel_ups.extend(vehicle.fuelup_set.all())

    if not fuel_ups:
      return 0

    return sum([fu.miles for fu in fuel_ups]) / sum([fu.gallons for fu in fuel_ups])

class Vehicle(models.Model):
  model = models.ForeignKey(Model)
  year = models.IntegerField()
  name = models.CharField(max_length=20)

  def __str__(self):
    return self.name

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
