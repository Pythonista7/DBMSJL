from django import forms
from .models import Jobs
from Accounts.models import Company

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
            
			"title",
			"category",
			"rec_email",
			"posting_loc",
			"requriments",
			"job_type",
			"posted_on",
			"deadline",
			"no_of_positions"]
        exclude=["company",'rec_email','no_of_applicants']
        
    """
    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(PostJobForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(PostJobForm, self).save(commit=False)
        inst.rec_email = self._user.email
        if commit:
            inst.save()
            self.save_m2m()
        return inst
    """

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


