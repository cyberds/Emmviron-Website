from django.db import models

class JobOpening(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    job_description = models.TextField()
    qualification = models.TextField()
    duties = models.TextField(null = True, blank=True)
    salary = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    contract_type = models.CharField(max_length=20, choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract')])
    closed = models.BooleanField(default=False)

    def formatted_qualifications(self):
        # Use this method to convert the qualifications text into an HTML list
        qualifications_list = [f"<li>{item.strip()}</li>" for item in self.qualifications.split('\n') if item.strip()]
        return "<ul>" + "".join(qualifications_list) + "</ul>"

    def formatted_duties(self):
        # Use this method to convert the qualifications text into an HTML list
        duties = [f"<li>{item.strip()}</li>" for item in self.duty.split('\n') if item.strip()]
        return "<ul>" + "".join(duties) + "</ul>"

    def __str__(self):
        return self.name



class TalenttaFormEntry(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    professional_skills = models.TextField()
    talentta_expectation = models.TextField()

    def __str__(self):
        return self.email



class Contacts(models.Model):
    SERVICE_CHOICES = (
        ('business_plan_financial_projection', 'Business Plan + Financial Projection'),
        ('business_plan_financial_model_pitch_deck', 'Business Plan + Financial Model (Cap Valuation) + Pitch Deck'),
        ('pitch_deck', 'Pitch Deck'),
        ('company_profile', 'Company Profile'),
        ('desktop_market_research', 'Desktop Market Research'),
        ('primary_market_research', 'Primary Market Research'),
        ('recruitment', 'Recruitment (We charge lesser than other firms)'),
        ('talent_management', 'Talent Management'),
        ('business_proposal', 'Business Proposal'),
        ('feasibility_study_report', 'Feasibility Study Report'),
        ('operational_setup', 'Operational Setup'),
        ('financial_model_alone', 'Financial Model alone'),
        ('business_training', 'Business Training for Executives/Team Members'),
        ('business_advisory', 'Business Advisory'),
        ('others', 'Others (Specify in the Subject)'),
    )


    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    business_name = models.CharField(max_length=200)

    requested_service = models.CharField(max_length=200, choices=SERVICE_CHOICES)
    subject = models.CharField(max_length=500)
    message = models.TextField()
    country = models.CharField(max_length = 500)
    state = models.CharField(max_length = 500)


    def __str__(self):
        return f"{self.first_name} {self.last_name} service: {self.requested_service}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"