"""NYCJobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import (
        register_company,
        job_create_view,
        register_home_view,
        recruiter_job_listing_view,
        applicant_job_listing_view,
        general_login_view,
        get_job_details,
        delete_job,
        company_profile_view,
        apply_view
        )

urlpatterns = [
    path("joblist/recruiter",recruiter_job_listing_view),
    path("joblist/applicant",applicant_job_listing_view),
    #path("login/",general_login_view),
    path("register/",register_home_view),
    path("register/newjob/",job_create_view),
    path("register/newcompany/",register_company),
    path("getjob/<int:id>/",get_job_details),
    path("delete/<int:job_id>/",delete_job),
    path("company/<str:company_name>/",company_profile_view),
    path("applySuccessful/<int:job_id>/",apply_view)
]
