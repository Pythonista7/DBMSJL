from django.contrib import admin
from django.urls import path,include
from .views import ApplicantProfileView,ApplicantProfileEditEduView,RecruiterProfileView,logout_view

urlpatterns = [
    path('Applicant/Profile',ApplicantProfileView),
    path('Applicant/Profile/edit/edu',ApplicantProfileEditEduView),
    path('Recruiter/Profile',RecruiterProfileView),
    path('logout/',logout_view)
]
