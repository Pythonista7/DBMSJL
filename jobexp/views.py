from django.shortcuts import render,redirect
from .forms import (PostJobForm,
        RegisterCompanyForm,
        RegisterRecruiterForm,
        ApplicantRegistrationForm
        )
# Create your views here.

def register_home_view(request,*args,**kwargs):
	return render(request,"register.html")

def applicant_signup_view(request,*args,**kwargs):
    form=ApplicantRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ApplicantRegistrationForm()
        #redirect('register_home_view')
    context={'form':form}
    return render(request,"applicant/signUpApplicant.html",context)

def job_create_view(request,*args,**kwargs):
    form=PostJobForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=PostJobForm()
        #redirect('register_home_view')
    context={'form':form}
    return render(request,"forms/create_job.html",context)

def register_company(request,*args,**kwargs):
    form=RegisterCompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=RegisterCompanyForm()
    context={'form':form}
    return render(request,"forms/register_company.html",context)

def register_recruiter(request,*args,**kwargs):
    form=RegisterRecruiterForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=RegisterRecruiterForm()
    context={'form':form}
    return render(request,"forms/register_recruiter.html",context)