from django.contrib import admin
from django.urls import path,include
from .views import ApplicantProfileView,RecruiterProfileView

urlpatterns = [
    path('Applicant/Profile',ApplicantProfileView),
    path('Recruiter/Profile',RecruiterProfileView),

]
