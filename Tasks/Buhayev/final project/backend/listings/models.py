from random import choices
from django.contrib.gis.db import models
from django.utils import timezone
from django.contrib.gis.geos import Point
from django.contrib.auth import get_user_model

User = get_user_model()
    
# Create your models here.
class Listing(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    choices_area = (
        ('Inner London', 'Inner London'),
        ('Outer London', 'Outer London')
    )
    area = models.CharField(max_length=20, blank=True, null=True, choices=choices_area)
    borough = models.CharField(max_length=50, blank=True, null=True)
    choices_listing_type = (
        ('House', 'House'),
        ('Apartment', 'Apartment'),
        ('Office', 'Office'),
    )
    listing_type = models.CharField(max_length=20, choices=choices_listing_type, null=False, blank=True)
    choices_property_status = (
        ('Sale', 'Sale'),
        ('Rent', 'Rent')
    )
    property_status = models.CharField(max_length=20, blank=True, null=True, choices=choices_property_status)
    price = models.DecimalField(max_digits=70, decimal_places = 0, null=True, blank=True)
    choices_rental_frequency = (
        ('Month', 'Month'),
        ('Week', 'Week'),
        ('Day', 'Day')
    )
    rental_frequency = models.CharField(max_length = 20, blank = True, null = True, choices = choices_rental_frequency)
    rooms = models.IntegerField(blank=True, null=True)
    furnished = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    cctv = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    date_posted = models.DateField(auto_now=True,blank=True, null=True)
    location = models.PointField(blank=True, null = True, srid=4326)
    latitude = models.FloatField(blank=True, null = True)
    longitude = models.FloatField(blank=True, null = True)
    picture = models.ImageField(blank=True, null = True, upload_to='pictures/%Y/%m/%d/')
    def __str__(self):
        return self.title
    
    
