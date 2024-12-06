import django
from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel


# Create your models here.

# class User(AbstractUser):
#     username=None
#     phone_number=models.CharField(max_length=12, unique=True)
#     is_phone_verified = models.BooleanField(default=False)
#     otp = models.CharField(max_length=6)
    
#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = []
#     objects = UserManager()
    
    
# class Profile(BaseModel):
#     user=models.OneToOneField(User, on_delete=models.CASCADE , related_name="profile")
#     is_email_verified = models.BooleanField(default=False)
#     email_token = models.CharField(max_length=6, null=True , blank=True)
#     Profile_img = models.FileField(upload_to = "hostpic")

class AdvatureMaster(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True ,null=True , limit_choices_to={'is_staff':True})
    adv_name=models.CharField(max_length=200)
    adv_details = models.TextField()
    adv_charges = models.PositiveIntegerField()
    
class ServiceMaster(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True ,null=True, limit_choices_to={'is_staff':True})
    service_name = models.CharField(max_length=200)
    service_details = models.TextField()
    service_cost = models.PositiveIntegerField()
    service_img =models.FileField(upload_to='servicesImg')

PERSON_CHOICES=[('1 Person','1 Person'),('2 People','2 People'),('3 People','3 People'),('4 People','4 People'),('5 People','5 People'),('6 People','6 People'),('7 People','7 People'),('8 People','8 People'),('9 People','9 People'),('10 People','10 People'),]   
class BookingMaster(BaseModel):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email= models.EmailField(max_length=254)
    phno= models.BigIntegerField()
    address = models.TextField()
    bookingDate = models.DateField(auto_now_add=True)
    stayTo = models.DateField(auto_now=True)
    stayFrom = models.DateField(auto_now=True)
    peopel = models.CharField(choices=PERSON_CHOICES,max_length=100)
    message = models.TextField()
    services = models.CharField( max_length=200)
    advature = models.CharField( max_length=200)
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

class contactMaster(models.Model):
    cname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=300)
    message = models.TextField()



