from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('resume/', ResumeTemplateView.as_view(), name='resume'),
    path('portfolio/', PortfolioTemplateView.as_view(), name='portfolio'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
]
