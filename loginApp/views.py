from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ApplicantRegistrationForm

# Create your views here.

def register_applicant(request,*args,**kwargs):
    form=ApplicantRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        #return redirect('/')
    else:
        form=ApplicantRegistrationForm()
    context={"form":form}
    return render(request,'applicant/signUpApplicant.html',context=context)