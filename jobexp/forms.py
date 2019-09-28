from django import forms
from .models import Jobs,Company,Recuiter,ApplicantProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostJobForm(forms.ModelForm):
    title       = forms.CharField(label='Job Title', 
                    widget=forms.TextInput(attrs={"placeholder": "Your Job title"}))

    requriments = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Enter detailed job requriments here ",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "ronumberws": 10,
                                    'cols': 150
                                }
                            )
                        )


    no_of_positions = forms.IntegerField(min_value=1,max_value=25)
    class Meta:
        model=Jobs
        fields=[		
            "company",
			"title",
			"category",
			"rec_email",
			"posting_loc",
			"requriments",
			"job_type",
			"posted_on",
			"deadline",
			"no_of_positions"]





class RegisterCompanyForm(forms.ModelForm):
    company_name=forms.CharField(label='Company Name', 
                    widget=forms.TextInput(attrs={"placeholder": "Comapny Name"}))
    biz_stream=forms.CharField(label="Industry/Business Stream")
    website=forms.URLField()
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Decribe your company here ",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "ronumberws": 10,
                                    'cols': 150
                                }
                            )
                        )
    def clean_company_name(self,*args,**kwargs):
        company_name=self.cleaned_data.get('company_name')
        #if company_name in queryset of all unique company names already registed throw validationException 
        if Company.objects.filter(company_name=company_name).exists():
            raise forms.ValidationError("Company is already Registered")
        else:
            return company_name    
    
    class Meta:
        model=Company
        fields=[
            "company_name",
            "biz_stream",
            "website",
            "description"
        ]




class RegisterRecruiterForm(forms.ModelForm):

    email=forms.EmailField()
    passwd=forms.PasswordInput()

    

    class Meta:
        model=Recuiter
        fields=[
            "email",
            "passwd",
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