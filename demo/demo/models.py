from django import models

class Flight(models.Model):
    destination = models.CharField(max_length=50)
    seat = models.IntegerField()

class Train(models.Model):
    Class = model.IntegerField()
    seat = model.IntegerField()
    destination = model.CharField(max_length=50)


class Cruise(models.Model):
    destination = model.CharField(max_length=50)
    