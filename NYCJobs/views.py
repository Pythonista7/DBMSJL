from django.shortcuts import render,redirect
from jobexp.models import Jobs

def opus_home(request):
    return render(request,"index.html")
