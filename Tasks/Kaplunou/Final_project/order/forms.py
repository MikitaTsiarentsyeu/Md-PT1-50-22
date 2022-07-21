from django import forms

from order.models import OrderItem


class AddQuantityForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']