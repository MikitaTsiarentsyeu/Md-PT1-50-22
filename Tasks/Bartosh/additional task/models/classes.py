from email.policy import default
from django.forms import CharField, DateTimeField, DecimalField, IntegerField


class User:
    user_name CharField(blank=False, max_lenght=50)

class User_group:
    group_name CharField(blank=False, max_lenght=50)
    user_name CharField(blank=False, max_lenght=50)
    
class Currency:
    currency_name CharField(blank=False, max_lenght=50)

class Place:

    CHOICE_TYPE= [('y', 'yes'),('n', 'no')]

    place_name CharField(blank=False, max_lenght=50)
    my_place - CharField(blank=False, max_lenght=1, default='y', choices=CHOICE_TYPE)
    savings - CharField(blank=False, max_lenght=1, default='n', choices=CHOICE_TYPE)

class Envelope:

    CHOICE_TYPE= [('y', 'yes'),('n', 'no')]

    envelope_name CharField(blank=False, max_lenght=50)
    income_or_expense
    limit IntegerField()
    common - harField(blank=False, max_lenght=1, default='n', choices=CHOICE_TYPE)
    savings - CharField(blank=False, max_lenght=1, default='n', choices=CHOICE_TYPE)

class Spending_plan:
    date DateTimeField()
    amount DecimalField()
    currency
    envelope
    priority IntegerField()
    comment CharField(max_lenght=140)

class Income_plan:
    date DateTimeField()
    amount IntegerField()
    currency
    place
    envelope
    comment CharField(max_lenght=140)

class Row:

    income_or_expense_type = [('+', 'income'),('-', 'expense')]

    date DateTimeField()
    amount DecimalField()
    currency 
    exchange_rate DecimalField()
    income_or_expense CharField(blank=False, max_lenght=1, choices= income_or_expense_type)
    place
    envelope
    user 
    comment  CharField(max_lenght=140)