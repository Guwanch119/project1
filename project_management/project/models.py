from django.db import models
from django.contrib.auth.models import User

class student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

# Create your models here.
