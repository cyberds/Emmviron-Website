from django import forms
from .models import Contacts

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = [
            'first_name', 'last_name', 'phone_number', 'email', 
            'business_name', 'requested_service', 'subject', 
            'message', 'country', 'state'
        ]
        widgets = {
            'requested_service': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'rows': 3}),
        }
