from django.db import models

# Create your models here.
class User(models.Model):
    useName = models.CharField(max_length=64)
    phoneNumber = models.IntegerField(max_length=10)