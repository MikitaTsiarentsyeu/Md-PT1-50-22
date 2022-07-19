from random import choices
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Review(models.Model):
    user_name = models.CharField(max_length=255, null=False, blank=True)
    review_date = models.DateField(auto_now=True, blank=True, null=True)
    review = models.TextField(max_length=2000, null=False, blank=True)
    
    def __str__(self):
        return f'review of {self.user_name} on {self.review_date}'
