from django.shortcuts import render,redirect,HttpResponse
from jobexp.models import Jobs
from django.contrib.auth.models import User
from django.contrib.auth import logout

def opus_home(request):
    #print('OPUS HOME')
    if request.user not in User.objects.all():
        #print("USer",request.user.username)
        #print("Not a user pls signUp or Login")
        return render(request,"index.html")
        #return redirect('/login')

    elif len(request.user.groups.all())==0:
        return HttpResponse("<h1>Error Ocuured user not registered.SignUp and try again </h1>") #redirect('/login')#

    elif(request.user.groups.all()[0].name == "Applicant"):
        return redirect("/accounts/Applicant/Profile")

    elif(request.user.groups.all()[0].name == "Recruiter"):
        return redirect("/accounts/Recruiter/Profile")

    else:
        return render(request,"index.html")


def logout_view(request,*args,**kwargs):
    logout(request)
    redirect("/accounts/login")

def registerNewClients(request,*args,**kwargs):
    return render(request,'signUpOption.html')