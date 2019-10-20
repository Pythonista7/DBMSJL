from django.contrib import admin

# Register your models here.
from .models import Jobs
from Accounts.models import ApplicantEdu

admin.site.register(Jobs)
admin.site.register(ApplicantEdu)
#admin.site.register(Company)
"""
admin.site.register(Recuiter)
admin.site.register(ApplicantProfile)
admin.site.register(ApplicantEdu)
admin.site.register(ApplicantExp)
admin.site.register(ApplicantSkills)
"""