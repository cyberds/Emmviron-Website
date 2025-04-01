from django.db import models
from django.utils.safestring import mark_safe
from django.core.validators import MinValueValidator, MaxValueValidator

class JobOpening(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    job_description = models.TextField()
    qualification = models.TextField()
    duties = models.TextField(null = True, blank=True)
    salary = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    contract_type = models.CharField(max_length=20, choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract')])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def formatted_qualifications(self):
        # Use this method to convert the qualifications text into an HTML list
        qualifications_list = [f"<li>{item.strip()}</li>" for item in self.qualification.split('\n') if item.strip()]
        return mark_safe("<ul>" + "".join(qualifications_list) + "</ul>")

    def formatted_duties(self):
        # Use this method to convert the qualifications text into an HTML list
        duties = [f"<li>{item.strip()}</li>" for item in self.duties.split('\n') if item.strip()]
        return mark_safe("<ul>" + "".join(duties) + "</ul>")

    def __str__(self):
        return self.name



class JobApplication(models.Model):
    job = models.ForeignKey('JobOpening', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    linkedin_profile = models.URLField(null=True, blank=True)
    bio = models.TextField()
    social_media_handles = models.TextField(null=True, blank=True)
    resume = models.FileField(upload_to='resumes/')
    passport_photo = models.ImageField(upload_to='passport_photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.job.name}"



class TalenttaFormEntry(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    professional_skills = models.TextField()
    talentta_expectation = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.email


    def __str__(self):
        return f"{self.first_name} {self.last_name} service: {self.requested_service}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"




class FAQ(models.Model):
    CATEGORY_CHOICES = (
        ('general', 'General'),
        ('funding', 'Funding & Investor'),
        ('additional', 'Additional Questions')
    )
    
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    featured = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} - {self.position}"


class Features(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Service (Pricing Feature)"
        verbose_name_plural = "Services (Pricing Features)"


class Pricing(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField()
    features = models.ManyToManyField(Features)
    is_popular = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.name} ({self.price or 'Not Specified'})"
    
    class Meta:
        verbose_name = "Pricing"
        verbose_name_plural = "Pricing Plans"


class Contacts(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    business_name = models.CharField(max_length=200)

    requested_service = models.ForeignKey(Features, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=500)
    message = models.TextField()
    country = models.CharField(max_length = 500)
    state = models.CharField(max_length = 500)
    contacted_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
      return f"{self.first_name} {self.last_name} service: {self.requested_service}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"