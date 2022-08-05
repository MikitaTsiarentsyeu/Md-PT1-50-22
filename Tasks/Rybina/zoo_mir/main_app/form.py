from django import forms

PROD_QUATITY_CHOICES = [(i, str(i)) for i in range (1, 6)]

class CartAddForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PROD_QUATITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)