from .models import FAQ, Testimonial

def faq_processor(request):
    testimonials = Testimonial.objects.all().order_by('-rating')
    faqs = FAQ.objects.filter(is_active=True)
    faq_categories = {
        'general': faqs.filter(category='general'),
        'funding': faqs.filter(category='funding'),
        'additional': faqs.filter(category='additional'),
    }
    return {
        "faqs": faqs,
        "faq_categories": faq_categories,
        "testimonials": testimonials,
    }
