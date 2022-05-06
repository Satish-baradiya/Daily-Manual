from datetime import date
from statistics import mode
from django.db import models

# Create your models here.


class Dairy(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    date = models.DateField(default=True)

    def __str__(self):
        return self.title
