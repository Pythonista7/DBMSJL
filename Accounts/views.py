from django.shortcuts import render,HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render,redirect,get_object_or_404

from .models import ApplicantProfile,ApplicantEdu,ApplicantExp,ApplicantSkills
from .forms import EducationForm,ExperienceForm,SkillsForm

def logout_view(request):
    logout(request)
    return redirect('/')

def ApplicantProfileView(request,*args,**kwargs):
    user=request.user
    user_profile=ApplicantProfile.objects.get(email=user.email) 
    #############################################
    try:
        user_edu=ApplicantEdu.objects.get(email=user.email)
    
    except:
        user_edu=ApplicantEdu.objects.none()
    #############################################
    try:
        user_exp=ApplicantExp.objects.get(email=user.email)
    
    except:
        user_exp=ApplicantExp.objects.none()
    
    #############################################
    try:
        user_skill=ApplicantSkills.objects.get(email=user.email)
    
    except:
        user_skill=ApplicantSkills.objects.none()

    context={"user":user,'user_profile':user_profile,'user_edu':user_edu,'user_exp':user_exp,'user_skill':user_skill}
    

    return render(request,'applicant/index.html',context=context)      #HttpResponse("<h1>APPLICANT PROFILE</h1>")


def ApplicantProfileCreateEduView(request,*args,**kwargs):
    if request.method =='POST':
        form=EducationForm(request.POST or None)
        ed=form.save(commit=False)
        ed.email=ApplicantProfile.objects.get(email=request.user.email) 


        ed.save()
        if form.is_valid():
            
            form.save()
        
            return redirect('/')
        else:
            return HttpResponse('<h1>form was invalid</h1>')

    else:
        form=EducationForm()
        context={"form":form}
        return render(request,'applicant/editApplicant.html',context=context)


def ApplicantProfileCreateExpView(request,*args,**kwargs):
    if request.method =='POST':
        form=ExperienceForm(request.POST or None)
        
        ed=form.save(commit=False)
        #print(request.user.email)
        #email=request.user.email#ed.email=request.user.email
        ed.email=ApplicantProfile.objects.get(email=request.user.email)
        #ApplicantExp.objects.filter(pk=email).update(total_exp=form.total_exp)
        #ApplicantExp.objects.filter(pk=email).update(start_date=form.start_date)
        #ApplicantExp.objects.filter(pk=email).update(end_date=form.end_date)
        #ApplicantExp.objects.filter(pk=email).update(company=form.company)
        #print("\n\n FORM SAVED \n\n",form.cleaned_data,"\n\n")
        form.save()
        if form.is_valid():
            
            form.save()
            print("\n\n FORM SAVED \n\n",form.cleaned_data,"\n\n")
        
            return redirect('/')
        else:
            return HttpResponse('<h1>form was invalid</h1>')

    else:
        form=ExperienceForm()
        context={"form":form}
        return render(request,'applicant/editApplicant.html',context=context)


def ApplicantProfileCreateSkillView(request,*args,**kwargs):
    if request.method =='POST':
        form=SkillsForm(request.POST or None)
        ed=form.save(commit=False)
        #print(request.user.email)
        #ed.email=request.user.email
        ed.email=ApplicantProfile.objects.get(email=request.user.email) 
        #print("\n\n FORM SAVED \n\n",form.cleaned_data,"\n\n")
        ed.save()
        if form.is_valid():
            
            form.save()
            print("\n\n FORM SAVED \n\n",form.cleaned_data,"\n\n")
        
            return redirect('/')
        else:
            return HttpResponse('<h1>form was invalid</h1>')

    else:
        form=SkillsForm()
        context={"form":form}
        return render(request,'applicant/editApplicant.html',context=context)





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