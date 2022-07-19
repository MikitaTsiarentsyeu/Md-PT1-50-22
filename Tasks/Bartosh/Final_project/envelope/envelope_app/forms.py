from django import forms
from .models import Row
#from django.core.exceptions import ValidationError


class AddRow(forms.ModelForm):

    class Meta:
        model = Row
        fields = ('amount', 'currency', 'exchange_rate', 'income_or_expense', 'place', 'envelope',  'user', 'comment')
        labels = {'exchange_rate':"Exchange rate", 'income_or_expense':"Income or expense"}


