from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ApplicantRegistrationForm

# Create your views here.

def register_applicant(request):
    form=ApplicantRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        mail_id=form.cleaned_data['email_id']
        #return redirect('/')
    else:
        form=ApplicantRegistrationForm()
    
    return render(request,'applicant/signUpApplicant.html',context={"form":form})