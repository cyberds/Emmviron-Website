from django import forms
from .models import Contacts, JobApplication

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


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['full_name', 'email', 'phone', 'linkedin_profile', 'bio', 'social_media_handles', 'resume', 'passport_photo']