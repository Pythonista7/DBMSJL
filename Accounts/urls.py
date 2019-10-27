from django.contrib import admin
from django.urls import path,include
from .views import (ApplicantProfileView,
                    ApplicantProfileEditEduView,
                    ApplicantProfileEditExpView,
                    RecruiterProfileView,
                    logout_view,
                    
                    )

urlpatterns = [
    path('Applicant/Profile',ApplicantProfileView),
    path('Applicant/Profile/edit/edu',ApplicantProfileEditEduView),
    path('Applicant/Profile/edit/exp',ApplicantProfileEditExpView),
    path('Recruiter/Profile',RecruiterProfileView),
    path('logout/',logout_view)
]
