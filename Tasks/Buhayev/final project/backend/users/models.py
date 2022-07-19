from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
    
class Profile(models.Model):
    seller = models.OneToOneField(User, on_delete=models.CASCADE)
    agency_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/%Y/%m/%d/', null=True, blank=True)
    
    def __str__(self):
        return f"profile of {self.seller.username}"
    