from .models import FAQ

def faq_processor(request):
    faqs = FAQ.objects.filter(is_active=True)
    faq_categories = {
        'general': faqs.filter(category='general'),
        'funding': faqs.filter(category='funding'),
        'additional': faqs.filter(category='additional')
    }
    return {
        "faqs": faqs,
        "faq_categories": faq_categories
    }
