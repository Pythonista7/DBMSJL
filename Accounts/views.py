from django.shortcuts import render,HttpResponse
from django.contrib.auth import login,logout,authenticate
from .forms import ApplicantRegistrationForm,RegisterRecruiterForm,LoginForm
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

def login_view(request,*args,**kwargs):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        user=form.save()
        login(request,user)
        return(HttpResponse("<h1>Logged in as "+"</h1"))
    else:
        print("INVALID LOGIN")
        form=LoginForm()
    context={'form':form}
    return render(request,"login.html",context)