from django.db import models
from eventbrite import Eventbrite

class category(models.Model):
    name = models.CharField(max_length=200)
    idNum = models.CharField(max_length=3)
    def __str__(self):
        return self.name
    def idNumber(self):
        return self.idNum
class Events(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
# Create your models here.
