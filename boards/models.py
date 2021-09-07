from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=500, default = 'image')
    details = models.TextField(max_length = 300, default = 'n/a')
    def __str__(self):
        return self.name
