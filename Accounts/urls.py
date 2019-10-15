from django.contrib import admin
from django.urls import path,include
from .views import ApplicantProfileView,RecruiterProfileView,logout_view

urlpatterns = [
    path('Applicant/Profile',ApplicantProfileView),
    path('Recruiter/Profile',RecruiterProfileView),
    path('logout/',logout_view)
]
