from django.shortcuts import render
from .forms import ApplicantRegistrationForm,RegisterRecruiterForm 
# Create your views here.

def applicant_signup_view(request,*args,**kwargs):
    form=ApplicantRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ApplicantRegistrationForm()
        #redirect('register_home_view')
    context={'form':form}
    return render(request,"applicant/signUpApplicant.html",context)

def register_recruiter(request,*args,**kwargs):
    form=RegisterRecruiterForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=RegisterRecruiterForm()
    context={'form':form}
    return render(request,"forms/register_recruiter.html",context)