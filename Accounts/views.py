from django.shortcuts import render,HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render,redirect

from .models import ApplicantProfile

def logout_view(request):
    logout(request)
    return redirect('/')


def ApplicantProfileView(request,*args,**kwargs):
    user=request.user
    user_profile=ApplicantProfile.objects.get(email=user.email) 
    context={"user":user,'user_profile':user_profile}
    return render(request,'applicant/index.html',context=context)      #HttpResponse("<h1>APPLICANT PROFILE</h1>")



def RecruiterProfileView(request,*args,**kwargs):
    username=request.user.email
    context={"username":username}
    return render(request,'recruiter/index.html',context=context)       #HttpResponse("<h1>RECRUITER PROFILE</h1>")




""" from django.contrib.auth import login,logout,authenticate
from .forms import ApplicantRegistrationForm,RegisterRecruiterForm,LoginForm
from django.contrib.auth.models import Group


# Create your views here.

def applicant_signup_view(request,*args,**kwargs):
    form=ApplicantRegistrationForm(request.POST or None)
    if form.is_valid():
        user=form.save()
        applicant_group = Group.objects.get(name='Applicant') 
        applicant_group.user_set.add(user)
        return HttpResponse("Applicant sucessfuly created")
        #form=ApplicantRegistrationForm()
        #redirect('register_home_view')
    context={'form':form}
    return render(request,"applicant/signUpApplicant.html",context)

def register_recruiter(request,*args,**kwargs):
    form=RegisterRecruiterForm(request.POST or None)
    if form.is_valid():
        print("REC FORM IS VALID")
        user=form.save()
        rec_group=Group.objects.get(name="Recruiter")
        #rec_group.user_set.add(user)
        return HttpResponse("Recruiter sucessfully created ")
        #form=RegisterRecruiterForm()
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
    return render(request,"login.html",context) """