from django.shortcuts import render,redirect

def opus_home(request):
    return render(request,"index.html")