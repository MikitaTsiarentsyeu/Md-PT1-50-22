from django.contrib import admin

from .models import User, User_group, Currency, Place, Envelope, Spending_plan, Income_plan, Row

# Register your models here.

admin.site.register(User)
admin.site.register(User_group)
admin.site.register(Currency)
admin.site.register(Place)
admin.site.register(Envelope)
admin.site.register(Spending_plan) 
admin.site.register(Income_plan)
admin.site.register(Row)