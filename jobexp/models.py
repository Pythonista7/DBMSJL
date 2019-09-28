from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from datetime import date

class Company(models.Model):
    company_name = models.CharField(primary_key=True, max_length=30)
    biz_stream = models.CharField(max_length=30, blank=True)
    website = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000, blank=True)

    class Meta:
        #managed = False
        db_table = 'COMPANY'


class Recuiter(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    passwd = models.CharField(max_length=128)
    company_name = models.ForeignKey(Company, models.DO_NOTHING, db_column='company_name')

    class Meta:
        #managed = False
        db_table = 'RECUITER'
        
class ApplicantProfile(models.Model):
    email_id = models.CharField(primary_key=True, max_length=50)
    applicant_passwd = models.CharField(max_length=128,blank=False, null=False)
    signup_date = models.DateField(db_column='signUp_date',default=date.today)  # Field name made lowercase. Autogent date
    first_nm = models.CharField(max_length=30,blank=False, null=False)
    last_nm = models.CharField(max_length=30,blank=False, null=False)
    location = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=30, blank=True)

    USERNAME_FIELD="email_id"

    class Meta:
        #managed = False
        db_table = 'APPLICANT_PROFILE'


class ApplicantSkills(models.Model):
    email = models.ForeignKey(ApplicantProfile, models.DO_NOTHING, primary_key=True)
    skill = models.CharField(max_length=30)

    class Meta:
        #managed = False
        db_table = 'APPLICANT_SKILLS'
        unique_together = (('email', 'skill'),)


class ApplicantEdu(models.Model):
    email = models.ForeignKey('ApplicantProfile', models.DO_NOTHING, primary_key=True)
    university = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    cgpa = models.FloatField()

    class Meta:
        #managed = False
        db_table = 'APPLICANT_EDU'


class ApplicantExp(models.Model):
    email = models.ForeignKey('ApplicantProfile', models.DO_NOTHING, primary_key=True)
    total_exp = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.CharField(max_length=30, blank=False)

    class Meta:
        #managed = False
        db_table = 'APPLICANT_EXP'
        unique_together = (('email', 'start_date', 'end_date'),)




class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, db_column='company')#,default="Google")
    title = models.CharField(max_length=30, blank=False)
    category = models.CharField(max_length=30, blank=True)
    rec_email = models.ForeignKey('Recuiter', models.DO_NOTHING, db_column='rec_email')
    posting_loc = models.CharField(max_length=30,default="Bangalore")
    requriments = models.CharField(max_length=1000)
    job_type = models.CharField(max_length=30, blank=True)
    posted_on = models.DateField(default=date.today)
    deadline = models.DateField(blank=True,null=True)
    no_of_positions = models.IntegerField(default=1)

    class Meta:
        #managed = False
        db_table = 'JOBS'

