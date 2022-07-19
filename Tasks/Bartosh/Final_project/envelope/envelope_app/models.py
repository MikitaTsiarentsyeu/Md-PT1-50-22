from django.db import models

class User(models.Model):
    user_name = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return self.user_name

class User_group(models.Model):
    group_name = models.CharField(blank=False, max_length=50)
    user_name = models.ForeignKey('User', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.group_name

class Currency(models.Model):   
    currency_name = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return self.currency_name 

#Place when I can find my money. For example wallet and debit card
class Place(models.Model):

    CHOICE_TYPE= [('y', 'yes'),('n', 'no')]

    place_name = models.CharField(blank=False, max_length=50)
    my_place = models.CharField(blank=False, default='y', choices=CHOICE_TYPE, max_length=1)
    savings = models.CharField(blank=False, default='n', choices=CHOICE_TYPE, max_length=1)

    def __str__(self):
        return self.place_name 

#Virtual envelopes which I use for action with money. For example food, transport
class Envelope(models.Model):

    CHOICE_TYPE= [('y', 'yes'),('n', 'no')]
    INCOME_OR_EXPENSE_TYPE = [('+', 'income'),('-', 'expense')]

    envelope_name = models.CharField(blank=False, max_length=50)
    income_or_expense = models.CharField(blank=False, choices = INCOME_OR_EXPENSE_TYPE, max_length=1)
    limit = models.IntegerField()
    common = models.CharField(blank=False, default='n', choices=CHOICE_TYPE, max_length=1)
    savings = models.CharField(blank=False, default='n', choices=CHOICE_TYPE,max_length=1)

    def __str__(self):
        return self.envelope_name 

class Spending_plan(models.Model):
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey('Currency', on_delete=models.DO_NOTHING)
    envelope = models.ForeignKey('Envelope', on_delete=models.DO_NOTHING)
    priority = models.IntegerField()
    comment = models.CharField(max_length=140)
   
class Income_plan(models.Model):
    date = models.DateTimeField()
    amount = models.IntegerField()
    currency = models.ForeignKey('Currency', on_delete=models.DO_NOTHING)
    place = models.ForeignKey('Place', on_delete=models.DO_NOTHING)
    envelope = models.ForeignKey('Envelope', on_delete=models.DO_NOTHING)
    comment = models.CharField(max_length=140)

class Row(models.Model):

    INCOME_OR_EXPENSE_TYPE = [('+', 'income'),('-', 'expense')]

    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey('Currency', on_delete=models.DO_NOTHING) 
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=2)
    income_or_expense = models.CharField(blank=False, choices= INCOME_OR_EXPENSE_TYPE, max_length=1)
    place = models.ForeignKey('Place', on_delete=models.DO_NOTHING)
    envelope = models.ForeignKey('Envelope', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING) 
    comment = models.CharField(blank=True, max_length=140)