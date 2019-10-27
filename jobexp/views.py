from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import (PostJobForm,
        RegisterCompanyForm,
        )
from .models import Jobs
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def register_home_view(request,*args,**kwargs):
	return render(request,"recruiter/register.html")

def job_create_view(request,*args,**kwargs):
    form=PostJobForm(request.POST or None)#user=request.user)
    if form.is_valid():
        rec_model=form.save(commit=False)
        user=User.objects.get(email=request.user.email)
        #if User.objects.get(email=request.user.email).group.filter(name="Recruiter"):
        rec_model.rec_email=user
        rec_model.save()

        form=PostJobForm()
        #redirect('register_home_view')
    context={'form':form}
    return render(request,"recruiter/create_job.html",context)

def recruiter_job_listing_view(request,*args,**kwargs):
    joblist=Jobs.objects.all()
    return render(request,"recruiter/job_listing.html",{"joblist":joblist})

def applicant_job_listing_view(request,*args,**kwargs):
    joblist=Jobs.objects.all()
    return render(request,"applicant/job_listing.html",{"joblist":joblist})


def register_company(request,*args,**kwargs):
    form=RegisterCompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=RegisterCompanyForm()
    context={'form':form}
    return render(request,"recruiter/register_company.html",context)

def general_login_view(request,*args,**kwargs):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('/')
    else:
        form=AuthenticationForm()
        context={"form":form}#"login":"LOGIN"}# or form.get_user().username)}
        return render(request,"login.html",context)