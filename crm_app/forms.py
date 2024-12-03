# crm_app/forms.py
from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'industry', 'email', 'phone', 'address', 'website']
