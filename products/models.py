from django.db import models
from base.models import BaseModel


# Create your models here.
   
# class Product(BaseModel):
#     product_name = models.CharField(max_length=100)
#     product_slug= models.SlugField(unique=True)
#     product_description= models.TextField()
#     product_price=models.IntegerField(default=0)
#     product_demo_price = models.IntegerField(default=0)
    
# class ProductMetaInformation(BaseModel):
#     Product = models.OneToOneField(Product,on_delete=models.CASCADE, related_name='meta_info')
#     product_measuring = models.CharField(max_length=100,null=True,blank=True,choices=(('KG','KG'),('ML','ML'),('L','L'),(None,None)))
#     product_quality = models.CharField(max_length=100,null=True,blank=True)
#     is_restirct= models.BooleanField(null=True,blank=True)
#     restrict_quantity = models.IntegerField()
    
# class PoroductImages(BaseModel):
#     product=models.ForeignKey(Product,on_delete=models.CASCADE , related_name="images")
#     product_images=models.ImageField(upload_to="products")