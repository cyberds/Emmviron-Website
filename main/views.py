from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ContactForm, JobApplicationForm
from .models import Contacts, JobOpening, Pricing

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

mailchimp = MailchimpMarketing.Client()
mailchimp.set_config({
  "api_key": "f034e61f40946857b234644f3c5b8047-us17",
  "server": "us17"
})


def add_to_mailchimp(first_name, last_name, email, service, subject, message, country, state, business_name, phone_number):
    list_id = "4441e65908"
    
    # Prepare the subscriber data
    subscriber_data = {
        "email_address": email,
        "status": "subscribed",  # Use 'subscribed' to add them to the list
        "merge_fields": {
            "FNAME": first_name,
            "LNAME": last_name,
            "SERVICE": str(service),
            "SUBJECT": subject,
            "MESSAGE": message,
            "COUNTRY": country,
            "STATE": state,
            "BNAME": business_name,
            "PHONE": phone_number
        }
    }
    
    try:
        response = mailchimp.lists.add_list_member(list_id, subscriber_data)
        print("Subscriber added successfully: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred while adding the subscriber: {}".format(error.text))


def home(request):
    # prices = sorted(Pricing.objects.all(), key=lambda x: int(x.price.replace('$', '').replace(',', '')))
    packages = Pricing.objects.all().order_by('order')
    from blog.models import Blog
    blogs = Blog.objects.all().order_by('-published_on')[:4]  # Get the latest 3 blog posts
    context = {
        # 'prices': packages,
        'blogs': blogs,
        }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract cleaned data from the form
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            service = form.cleaned_data['requested_service']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            country = form.cleaned_data['country']
            state = form.cleaned_data['state']
            business_name = form.cleaned_data['business_name']
            phone_number = form.cleaned_data['phone_number']

            # Try to add the subscriber to Mailchimp
            try:
                add_to_mailchimp(first_name, last_name, email, service, subject, message, country, state, business_name, phone_number)
            except Exception as e:
                messages.error(request, f"An error occurred while adding to Mailchimp: {str(e)}")
                
            
            # Save the form data to the database
            form.save()
            
            messages.success(request, 'Your form was submitted successfully!')
            return redirect('contact')  # Redirect after successful submission to avoid resubmitting on refresh
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})


def business_plan(request):
    # prices = sorted(Pricing.objects.all(), key=lambda x: int(x.price.replace('$', '').replace(',', '')))
    prices = Pricing.objects.all().order_by("order")
    context = {
        'prices': prices
    }
    return render(request, 'main/business_plan.html', context)

def schedule_meeting(request, plan_id):
    plan = get_object_or_404(Pricing, id=plan_id)
    context = {
        'plan': plan,
        'calendly_url': settings.CALENDLY_URL
    }
    return render(request, 'main/schedule_meeting.html', context)

def career(request):
    messages.info(request, "We've now moved our jobs to our partners at Talentta for a better experience")
    return render(request, 'main/redirect.html')

def job_application(request, id):
    job = get_object_or_404(JobOpening, id=id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('career')  # Replace 'career' with your job listings page URL name
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = JobApplicationForm()

    context = {
        'job': job,
        'form': form,
    }
    return render(request, 'main/job_application_page.html', context)

def financial_model(request):
    return render(request, 'main/financial_model.html')

def market_research(request):
    return render(request, 'main/market_research.html')

def operational_setup(request):
    return render(request, 'main/operational_setup.html')

def pitch_deck(request):
    return render(request, 'main/pitch_deck.html')

def strategic_business(request):
    return render(request, 'main/strategic_business.html')

def talent_n_recruitment(request):
    return render(request, 'main/talent_n_recruitment.html')
