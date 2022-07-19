from django.contrib import admin
from django.contrib.auth import get_user_model
from users.models import User
from .models import Profile
# Register your models here.

User = get_user_model()
admin.site.register(User)
admin.site.register(Profile)


