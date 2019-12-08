from django.db import models
from django.contrib.auth.models import User
from datetime import date
from Accounts.models import Recuiter,Company,ApplicantProfile


class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, models.CASCADE, db_column='company')#,default="Google")
    title = models.CharField(max_length=30, blank=False)
    category = models.CharField(max_length=30, blank=True)
    rec_email = models.ForeignKey(User, models.CASCADE, db_column='email')
    posting_loc = models.CharField(max_length=30,default="Bangalore")
    requriments = models.CharField(max_length=1000)
    job_type = models.CharField(max_length=30, blank=True)
    posted_on = models.DateField(default=date.today)
    deadline = models.DateField(blank=True,null=True)
    no_of_positions = models.IntegerField(default=1)
    no_of_applicants=models.IntegerField(default=0)
    class Meta:
        db_table = 'JOBS'


class ApplicantAppliedJobs(models.Model):
    email=models.OneToOneField(ApplicantProfile,on_delete=models.CASCADE,primary_key=True)
    job_id=models.ForeignKey(Jobs,on_delete=None)#models.IntegerField()
    applied_date=models.DateField()

    class Meta:
        db_table = 'APPLICANT_APPLIED'
        unique_together = (('email', 'job_id'),)