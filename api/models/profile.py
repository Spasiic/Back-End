from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/', blank=True, null=True)
    birth =  models.DateField(blank=True, null=True)

    def __str__(self): 
            return str(self.user)