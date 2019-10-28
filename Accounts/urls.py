from django.contrib import admin
from django.urls import path,include
from .views import (ApplicantProfileView,
                    ApplicantProfileCreateEduView,
                    ApplicantProfileCreateExpView,
                    ApplicantProfileCreateSkillView,
                    RecruiterProfileView,
                    logout_view,
                    
                    )

urlpatterns = [
    path('Applicant/Profile',ApplicantProfileView),
    path('Applicant/Profile/edit/edu',ApplicantProfileCreateEduView),
    path('Applicant/Profile/edit/exp',ApplicantProfileCreateExpView),
    path('Applicant/Profile/edit/skills',ApplicantProfileCreateSkillView),
    path('Recruiter/Profile',RecruiterProfileView),
    path('logout/',logout_view)
]
