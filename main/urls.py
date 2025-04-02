from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('schedule/<int:plan_id>/', views.schedule_meeting, name='schedule_meeting'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('business_plan/', views.business_plan, name='business_plan'),
    path('career/', views.career, name='career'),
    path('career/<int:id>/', views.job_application, name='job_application'),
    path('financial_model/', views.financial_model, name='financial_model'),
    path('market_research/', views.market_research, name='market_research'),
    path('operational_setup/', views.operational_setup, name='operational_setup'),
    path('pitch_deck/', views.pitch_deck, name='pitch_deck'),
    path('strategic_business/', views.strategic_business, name='strategic_business'),
    path('talent_n_recruitment/', views.talent_n_recruitment, name='talent_n_recruitment'),
]