from django.shortcuts import render,redirect
from jobexp.models import Jobs

def opus_home(request):
    return render(request,"index.html")

def global_job_list(request):
    joblist=Jobs.objects.all()
    return render(request,"job_listing.html",{"joblist":joblist})