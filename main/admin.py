from django.contrib import admin
from .models import FAQ, JobOpening, Contacts


class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'job_description', 'qualification', 'salary', 'contract_type', 'is_active')
    search_fields = ('name', 'qualification', 'job_description')

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'business_name', 'phone_number', 'email', 'requested_service', 'subject')
    search_fields = ('first_name', 'last_name', 'business_name', 'phone_number', 'email', 'requested_service', 'subject')


class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "category", "is_active", "created_at")
    list_filter = ("is_active",)


admin.site.register(JobOpening, JobOpeningAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(FAQ, FAQAdmin)