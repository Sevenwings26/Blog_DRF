from django.db import models

# users are going to make a post 
from django.contrib.auth.models import User

# to track time of user's post
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



