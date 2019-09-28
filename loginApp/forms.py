from django import forms
from django.contrib.auth.models import User
from jobexp.models import ApplicantProfile
from django.contrib.auth.forms import UserCreationForm


class ApplicantRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    first_nm=forms.CharField(label="First Name")
    last_nm=forms.CharField(label="Last Name")
    location=forms.CharField()
    gender=forms.ChoiceField(choices=('Male','Female','Other'))
    class Meta:
        model=ApplicantProfile
        fields=[
            "first_nm",
            "last_nm",
            "email_id",
            "applicant_passwd",
            "location",
            "gender"
        ]
