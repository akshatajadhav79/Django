from django.db import models
import uuid


# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(default=uuid.uuid4 , editable=False , primary_key=True )
    created_on=models.DateField(auto_now_add=True)
    updated_at= models.DateField(blank=True,auto_now=True)

    
    class Meta:
        #for To trite BaseModel as baseclass not as model
        abstract=True