from django.contrib import admin
from django.urls import path,include
from .views import (
        register_recruiter,
        applicant_signup_view,
        login_view
        )

#app_name="products"
urlpatterns = [
    path("register/applicant",applicant_signup_view),
    path("register/recruiter",register_recruiter),
    path("login/",login_view)
]
