from django.shortcuts import render,redirect
from jobexp.models import Jobs
from django.contrib.auth.models import User
from django.contrib.auth import logout

def opus_home(request):

    if request.user not in User.objects.all():
        #print("USer",request.user.username)
        print("Not a user pls signUp or Login")
        return redirect('/login')

    elif(request.user.groups.all()[0].name == "Applicant"):
        return redirect("/accounts/Applicant/Profile")

    elif(request.user.groups.all()[0].name == "Recruiter"):
        return redirect("/accounts/Recruiter/Profile")

    else:
        return render(request,"index.html")


def logout_view(request,*args,**kwargs):
    logout(request)
    redirect("/accounts/login")
