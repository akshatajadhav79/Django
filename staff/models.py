from django.db import models

# Create your models here.

class staffTypesMaster(models.Model):
    STid = models.AutoField(unique=True , primary_key=True)
    Tname = models.CharField(max_length=250)
     

class staffMaster(models.Model):
    sid = models.AutoField(unique=True, primary_key=True)
    first_name = models.CharField(max_length= 200)
    last_name = models.CharField( max_length=250)
    email = models.EmailField( max_length=254)
    address = models.TextField()
    contact = models.BigIntegerField()
    hiredDate = models.DateField( auto_now=False, auto_now_add=False)
    position = models.ForeignKey(staffTypesMaster, on_delete=models.CASCADE)
    pic = models.FileField( upload_to="staffProfileImg")
    DOB = models.DateField(auto_now=False, auto_now_add=False)

class MenuMaster(models.Model):
    MenuId= models.AutoField(primary_key=True)
    MenuName = models.CharField(max_length=255)
    sub_menu_id = models.IntegerField()
    
    def __str__(self):
        return self.MenuName


