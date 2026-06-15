from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 20, blank = False)
    surname = models.CharField(max_length = 20, blank = False)
    email = models.EmailField(max_length = 20, blank = False)
    phone = models.CharField(max_length = 12, blank = False)