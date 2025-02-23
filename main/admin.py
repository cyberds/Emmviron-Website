from django.contrib import admin
from .models import FAQ, JobOpening, Contacts, Testimonial, Pricing, Features


class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'job_description', 'qualification', 'salary', 'contract_type', 'is_active')
    search_fields = ('name', 'qualification', 'job_description')

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'business_name', 'phone_number', 'email', 'requested_service', 'subject')
    search_fields = ('first_name', 'last_name', 'business_name', 'phone_number', 'email', 'requested_service', 'subject')


class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "category", "is_active", "created_at")
    list_filter = ("is_active",)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "content", "image")
    search_fields = ("name", "position", "content")
    list_filter = ("position",)

class FeaturesAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)

class PricingAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_popular")
    search_fields = ("name", "price", "is_popular")
    list_filter = ("price", "is_popular")


admin.site.register(JobOpening, JobOpeningAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Pricing, PricingAdmin)
admin.site.register(Features, FeaturesAdmin)