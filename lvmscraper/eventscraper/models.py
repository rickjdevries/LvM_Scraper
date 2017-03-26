from django.db import models

class Event(models.Model):
    venue = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    date  = models.DateField()
    time  = models.CharField(max_length=30)
    URL   = models.CharField(max_length=80)
