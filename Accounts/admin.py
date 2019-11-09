from django.contrib import admin
from .models import ApplicantProfile,Recuiter,Company,SiteStats
# Register your models here.

admin.site.register(ApplicantProfile)
admin.site.register(Recuiter)
admin.site.register(Company)
admin.site.register(SiteStats)

