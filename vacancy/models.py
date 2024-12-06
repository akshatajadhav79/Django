from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class VaccancyMaster(models.Model):
    vid=models.AutoField(unique=True ,primary_key=True)
    vaccancyName = models.CharField( max_length=250)
    vaccancyInfo = models.TextField()
    postedDate = models.DateField(auto_now_add=True)
    user = models.ManyToManyField(User) 
    vpic = models.ImageField(upload_to='vaccancy_pictures', null=True, blank=True)
    
class CandidateMaster(models.Model):
    cid = models.AutoField(unique=True ,primary_key=True)
    cname = models.CharField(max_length=255)
    cresume = models.FileField(upload_to='CandidateResume')
    applydate = models.DateField(auto_now_add=True)
    vacancy = models.ForeignKey(VaccancyMaster,on_delete=models.CASCADE)
    