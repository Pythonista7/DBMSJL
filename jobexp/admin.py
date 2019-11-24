from django.contrib import admin

# Register your models here.
from .models import Jobs
from Accounts.models import ApplicantEdu,ApplicantExp,ApplicantSkills
from jobexp.models import ApplicantAppliedJobs

admin.site.register(Jobs)
admin.site.register(ApplicantEdu)
admin.site.register(ApplicantSkills)
admin.site.register(ApplicantExp)
admin.site.register(ApplicantAppliedJobs)

#admin.site.register(Company)
"""
admin.site.register(Recuiter)
admin.site.register(ApplicantProfile)
admin.site.register(ApplicantEdu)
admin.site.register(ApplicantExp)
admin.site.register(ApplicantSkills)
"""