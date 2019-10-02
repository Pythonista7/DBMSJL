from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(primary_key=True, max_length=30)
    biz_stream = models.CharField(max_length=30, blank=True)
    website = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000, blank=True)

    class Meta:
        #managed = False
        db_table = 'COMPANY'

    def __str__(self):
        return self.company_name

class Recuiter(AbstractBaseUser):#models.Model):
    email = models.EmailField(primary_key=True, max_length=50)
    company_name = models.ForeignKey(Company, models.DO_NOTHING, db_column='company_name')
 
    username 				= models.CharField(max_length=30, unique=False)
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    USERNAME_FIELD="email"

    class Meta:
        #managed = False
        db_table = 'RECUITER'
        
class ApplicantManager(BaseUserManager):

    def create_user(self,email_id,password=None):
        if not email_id:
            raise ValueError('User must have an email id .')
        if not password:
            raise ValidationError("Users must have password")
            
        user=self.model(
            email=self.normalize_email(email_id),
        )
        user.set_password(password) #set or change password like this
        user.save(using=self._db)
        return user
    


class ApplicantProfile(AbstractBaseUser): #(models.Model):
    email_id = models.EmailField(primary_key=True, max_length=50)
    location = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=30, blank=False)

    username 				= models.CharField(max_length=30, unique=True)
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)

    USERNAME_FIELD="email_id"
    objects=ApplicantManager

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
    email = models.ForeignKey(ApplicantProfile, models.DO_NOTHING, primary_key=True)
    university = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    cgpa = models.FloatField()

    class Meta:
        #managed = False
        db_table = 'APPLICANT_EDU'


class ApplicantExp(models.Model):
    email = models.ForeignKey(ApplicantProfile, models.DO_NOTHING, primary_key=True)
    total_exp = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.CharField(max_length=30, blank=False)

    class Meta:
        #managed = False
        db_table = 'APPLICANT_EXP'
        unique_together = (('email', 'start_date', 'end_date'),)
