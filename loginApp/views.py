from django.shortcuts import HttpResponse,render,redirect
from django.contrib import messages
from .forms import ApplicantRegistrationForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import Group

# Create your views here.

def login_view(request,*args,**kwargs):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        user=form.save()
        applicant_group = Group.objects.get(name='Applicant') 
        applicant_group.user_set.add(user)
        login(request,user)
        return redirect('/')
        #return HttpResponse("<h1>SucessFully logged in as "+user.email+"</h1>")
    else:
        for msg in form.error_messages:
            print(form.error_messages[msg])
             
    form=UserCreationForm()
    context={"form":form}
    return render(request,'login.html',context=context)