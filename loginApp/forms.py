from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm#,AuthenticationForm
from django.contrib.auth.models import User

class ApplicantRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    location=forms.CharField()
    gender=forms.ChoiceField(choices=(('Male','Male'),('Female','Female'),('Other','Other')))
    class Meta:
        model=User
        fields=[
            "email",
            "username", 
            "password1",
            "password2",
            "location",
            "gender"
        ]

class RecruiterRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    company=forms.ChoiceField(choices=(("Google","Google"),("FB","FB")))
    class Meta:
        model=User
        fields=[
            "email",
            "username", 
            "password1",
            "password2",
            "company"
        ]


