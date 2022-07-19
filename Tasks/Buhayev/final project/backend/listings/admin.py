from django.contrib import admin
from listings.models import Listing
# from .forms import ListingForm

# Register your models here.

# class ListingAdmin(admin.ModelAdmin):
#     form = ListingForm

admin.site.register(Listing)
