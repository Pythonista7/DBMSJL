from django.forms import ModelForm
from .models import ApplicantEdu
from django import forms
from django.contrib.admin.widgets import AdminDateWidget


class EducationForm(ModelForm):
    start_date= forms.DateField(widget=AdminDateWidget)
    end_date=forms.DateField(widget=AdminDateWidget)
    class Meta:
        model=ApplicantEdu
        requried=['university',"major","start_date","end_date","cgpa"]
        exclude=['email']        
        

























""" from django import forms
from .models import Recuiter,ApplicantProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    
    class Meta:
        model=Recuiter#ApplicantProfile
        fields=[
            "username",
            "password",
        ]


class RegisterRecruiterForm(UserCreationForm):

    email=forms.EmailField()
    

    class Meta:
        model=Recuiter
        fields=[
            "username",
            "email",
            "company_name"
        ]


class ApplicantRegistrationForm(UserCreationForm):
    email_id=forms.EmailField()
    location=forms.CharField()
    gender=forms.ChoiceField(choices=[("Male","Male"),("Female","Female")])
    class Meta:
        model=ApplicantProfile
        fields=[
            "email_id",
            "username",
            "location",
            "gender"
        ]
     """