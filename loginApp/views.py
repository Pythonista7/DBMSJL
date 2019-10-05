from django.shortcuts import HttpResponse,render,redirect
from django.contrib import messages
from .forms import ApplicantRegistrationForm,RecruiterRegistrationForm
from Accounts.models import ApplicantProfile,Recuiter

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import Group,User
from .forms import ApplicantRegistrationForm
# Create your views here.


def general_login_view(request,*args,**kwargs):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if user.group.name=="Applicant":
                return redirect('applicant/index.html')
            else:
                return redirect('recruiter/index.html')
    else:
        form=AuthenticationForm()
        context={"form":form}#"login":"LOGIN"}# or form.get_user().username)}
        return render(request,"login.html",context)

def applicant_register_login_view(request,*args,**kwargs):
    form=ApplicantRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        
        #username = form.cleaned_data.get('username')
        email= form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        raw_password2 = form.cleaned_data.get('password2')
        if raw_password==raw_password2:
            user = authenticate(username=email, password=raw_password)
            #log the user in
            login(request, user)
            #Add the user to applicant group 
            applicant_group = Group.objects.get(name='Applicant') 
            user=User.objects.get(email=email)
            applicant_group.user_set.add(user)
            #save other data to Account.models
            applicant=ApplicantProfile()
            applicant.email=form.cleaned_data.get('email')
            applicant.username=form.cleaned_data.get('username')
            applicant.gender=form.cleaned_data.get('gender')
            applicant.location=form.cleaned_data.get('location')
            return redirect('applicant/index.html')
            #return HttpResponse("<h1>SucessFully logged in as "+user.email+"</h1>")
    else:
        
        for msg in form.error_messages:
            print(form.error_messages[msg])
             
    form=ApplicantRegistrationForm()
    context={"form":form}
    return render(request,'login.html',context=context)


def recruiter_register_login_view(request,*args,**kwargs):
    form=RecruiterRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        email= form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        raw_password2 = form.cleaned_data.get('password2')
        if raw_password==raw_password2:
            user = authenticate(username=email, password=raw_password)
            #log the user in
            login(request, user)
            #Add the user to applicant group 
            rec_group = Group.objects.get(name='Recruiter') 
            user=User.objects.get(email=email)
            rec_group.user_set.add(user)
            #save other data to Account.models
            rec=Recuiter()
            rec.email=form.cleaned_data.get('email')
            rec.username=form.cleaned_data.get('username')
            rec.company=form.cleaned_data.get('company')
            rec.save()
            return redirect('recruiter/index.html')
            #return HttpResponse("<h1>SucessFully logged in as "+user.email+"</h1>")
    else:
        
        for msg in form.error_messages:
            print(form.error_messages[msg])
             
    form=RecruiterRegistrationForm()
    context={"form":form}
    return render(request,'login.html',context=context)