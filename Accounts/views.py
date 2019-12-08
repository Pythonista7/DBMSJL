from django.shortcuts import render,HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render,redirect,get_object_or_404

from .models import ApplicantProfile,ApplicantEdu,ApplicantExp,ApplicantSkills,Recuiter
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
    try:
        email=ApplicantProfile.objects.get(email=request.user.email) 
        if ApplicantEdu.objects.get(email=email):
                form=EducationForm(request.POST or None,instance=ApplicantEdu.objects.get(email=email))
                if form.is_valid():
                    form.save()
                    return redirect('/')
    except:
        pass

    print('\n\n\nNO USER EDU, CREATE ONE \n\n\n\n')

    if request.method =='POST':
        form=EducationForm(request.POST or None)
        
        if form.is_valid():
            ed=form.save(commit=False)
            ed.email=ApplicantProfile.objects.get(email=request.user.email) 
            ed.save()
            form.save()
        
            return redirect('/')
        else:
            return HttpResponse('<h1>form was invalid</h1>')

    else:
        form=EducationForm()
        context={"form":form}
        return render(request,'applicant/editApplicant.html',context=context)


def ApplicantProfileCreateExpView(request,*args,**kwargs):
    try:
        email=ApplicantProfile.objects.get(email=request.user.email) 
        if ApplicantExp.objects.get(email=email):
                #return redirect('/')
                #If the entry already exists then we need to update it 
                form=ExperienceForm(request.POST or None,instance=ApplicantExp.objects.get(email=email))
                if form.is_valid():
                    form.save()
                    return redirect('/')

    except:
        pass

    print('\n\n\nNO USER EXP, CREATE ONE \n\n\n\n')

    if request.method =='POST':
        form=ExperienceForm(request.POST or None)
        
        if form.is_valid():
            ed=form.save(commit=False)
            ed.email=ApplicantProfile.objects.get(email=request.user.email) 
            ed.save()
            form.save()
        
            return redirect('/')
        else:
            return HttpResponse('<h1>form was invalid</h1>')

    else:
        form=ExperienceForm()
        context={"form":form}
        return render(request,'applicant/editApplicant.html',context=context)

def ApplicantProfileCreateSkillView(request,*args,**kwargs):
    try:
        email=ApplicantProfile.objects.get(email=request.user.email) 
        if ApplicantSkills.objects.get(email=email):
                return redirect('/')
    except:
        pass

    print('\n\n\nNO USER SKILLS, CREATE SOME \n\n\n\n')

    if request.method =='POST':
        form=SkillsForm(request.POST or None)
        
        if form.is_valid():
            ed=form.save(commit=False)
            ed.email=ApplicantProfile.objects.get(email=request.user.email) 
            ed.save()
            form.save()
        
            return redirect('/')
        else:
            return HttpResponse('<h1>form was invalid</h1>')

    else:
        form=SkillsForm()
        context={"form":form}
        return render(request,'applicant/editApplicant.html',context=context)



def RecruiterProfileView(request,*args,**kwargs):
    username=request.user.email
    #try:
    context={"username":username,"user":Recuiter.objects.filter(email=username) or None}
    if context["user"]==None:
        return HttpResponse("<h3>Invalid User.Please Sign Up before login.</h3>")
    #if username in Recuiter.objects.username.all():
    return render(request,'recruiter/index.html',context=context)       
    #else:
    #    return redirect("/accounts/logout/")
    #except:
    #    return redirect("/accounts/logout/")


