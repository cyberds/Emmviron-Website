from main.models import Features

def populate_features():
    services = [
        'Business Plan + Financial Projection',
        'Business Plan + Financial Model (Cap Valuation) + Pitch Deck',
        'Company Profile',
        'Desktop Market Research',
        'Primary Market Research',
        'Recruitment',
        'Talent Management',
        'Business Proposal',
        'Feasibility Study Report',
        'Operational Setup',
        'Financial Model alone',
        'Business Training for Executives/Team Members',
        'Business Advisory',
        'Others'
    ]
    for service in services:
        Features.objects.create(name=service)
    print("Features populated successfully.")