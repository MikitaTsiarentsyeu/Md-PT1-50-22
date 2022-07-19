from django.contrib import admin
from django.contrib.auth import get_user_model
from reviews.models import Review
# Register your models here.
User = get_user_model()
admin.site.register(Review)