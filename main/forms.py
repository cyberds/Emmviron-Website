from django import forms
from .models import Contacts, JobApplication, Features

class ContactForm(forms.ModelForm):
    requested_service = forms.ModelChoiceField(
        queryset=Features.objects.all(),
        empty_label="Select a service",
        widget=forms.Select(attrs={'class': 'form-control'}) 
    )
    class Meta:
        model = Contacts
        fields = [
            'first_name', 'last_name', 'phone_number', 'email', 
            'business_name', 'requested_service', 'subject', 
            'message', 'country', 'state'
        ]
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 3, 
                'class': 'form-control',
                'style': 'min-height: 100px;'
                }),
        }


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['full_name', 'email', 'phone', 'linkedin_profile', 'bio', 'social_media_handles', 'resume', 'passport_photo']