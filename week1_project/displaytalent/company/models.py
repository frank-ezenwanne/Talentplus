from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    registered = models.BooleanField(default=True)