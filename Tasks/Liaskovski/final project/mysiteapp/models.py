import email
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False, primary_key=True)

    def __str__(self):
        return self.email

class Post(models.Model):
    POST_TYPES = [('c','comercial'),('a','authored')]

    title = models.CharField(blank=False, max_length=100)
    subtitle = models.CharField(max_length=200)
    content = models.TextField(blank=False)
    issued = models.DateField()
    post_type = models.CharField(blank=False,max_length=1, choices=POST_TYPES)
    phone = models.IntegerField(null=True)
    email_adress = models.EmailField(blank=False,null=True)
 

    author = models.ForeignKey('Author', on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'