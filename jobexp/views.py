from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User,Group
from .forms import (PostJobForm,
        RegisterCompanyForm,
        )
from .models import Jobs
from Accounts.models import ApplicantAppliedJobs
from Accounts.models import Recuiter,Company,ApplicantProfile
import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.db import connection

# Create your views here.

def register_home_view(request,*args,**kwargs):
	return render(request,"recruiter/register.html")

def job_create_view(request,*args,**kwargs):
    form=PostJobForm(request.POST or None)#user=request.user)
    if form.is_valid():
        ##NOTE THIS IS JOB MODEL
        job_model=form.save(commit=False)
        user=User.objects.get(email=request.user.email)
        #User.objects.raw(''' SELECT * FROM USER WHERE email = $ ''',request.user.email)
        #if User.objects.get(email=request.user.email).group.filter(name="Recruiter"):
        job_model.rec_email=user
        #with connection.cursor() as cursor:
        #    job_model.company=cursor.execute("SELECT company_name from RECUITER WHERE email = %s",[user.email])
        job_model.company=Recuiter.objects.get(email=user.email).company_name
        job_model.save()

        form=PostJobForm()
        #redirect('register_home_view')
    context={'form':form}
    return render(request,"recruiter/create_job.html",context)

def recruiter_job_listing_view(request,*args,**kwargs):
    joblist=Jobs.objects.raw("SELECT * FROM JOBS")  #Jobs.objects.all()
    return render(request,"recruiter/job_listing.html",{"joblist":joblist})

def applicant_job_listing_view(request,*args,**kwargs):
    joblist=Jobs.objects.raw("SELECT * FROM JOBS") #Jobs.objects.all()
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


def get_job_details(request,id):
    job=Jobs.objects.get(job_id=id)
    this_rec_job=False

    context={'job':job,"this_rec_job":False,"job_id":id}
    
    if is_Applicant(request.user):
        qs=ApplicantAppliedJobs.objects.filter(email=request.user.email,job_id=id)
        if qs.exists():
            context={'job':job,"this_rec_job":False,"job_id":id,"Applied":True}
            return render(request,'applicant/job_desc.html',context)
        else:
            context={'job':job,"this_rec_job":False,"job_id":id,"Applied":False}
            return render(request,'applicant/job_desc.html',context)

    else:
        #print(f"\n\n\n {request.user.username} \t\t {job.rec_email}  \n\n\n")
        if str(job.rec_email) == str(request.user.username):
            context={'job':job,"this_rec_job":True,"job_id":id}
            return render(request,'recruiter/job_desc.html',context)
        else:
            #return HttpResponse("You shouldnt be seeing this page, if you are please report to dev.")
            return render(request,'recruiter/job_desc.html',context)

def is_Applicant(user):
    return user.groups.filter(name='Applicant').exists()

#Try to use a trigger instead of this function 
def delete_job(request,job_id):
    #Jobs.objects.filter(job_id=job_id).delete()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM JOBS WHERE job_id = %s",[job_id])
    return redirect('/jobs/joblist/recruiter')

def company_profile_view(request,company_name):
    
    c=Company.objects.get(company_name=company_name)
    context={"company":c}
    #print("\n\n\nIT WAS HERE\n\n")
    return render(request,'company.html',context=context)


def apply_view(request,job_id):

    #increment job count
    print(job_id)
    #job=Jobs.objects.raw("UPDATE JOBS SET no_of_applicants=no_of_applicants+1 FROM JOBS WHERE job_id = %s",[job_id])#
    with connection.cursor() as cursor:
        cursor.execute("UPDATE JOBS SET no_of_applicants=no_of_applicants+1 WHERE job_id= %s",[job_id])
    
    #job=Jobs.objects.get(job_id=job_id)
    #print(job.no_of_applicants)
    #job.no_of_applicants=job.no_of_applicants+1
    #print(job.no_of_applicants)
    #job.save()

    #save list of job_ids to which a applicant has applied
    reg=ApplicantAppliedJobs()
    #umail=request.user.email
    #reg.email=cursor.execute("SELECT email FROM APPLICANT_PROFILE WHERE email = %s",[umail])
    #ApplicantProfile.objects.raw("SELECT * FROM APPLICANT_PROFILE WHERE email = %s ",[umail])  #ApplicantProfile.objects.get(email=request.user.email)
    reg.email=ApplicantProfile.objects.get(email=request.user.email)
    reg.job_id=job_id
    reg.applied_date=datetime.datetime.now()
    reg.save()

    return redirect('/')