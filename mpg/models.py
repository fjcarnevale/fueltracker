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
