from base.emails import  send_account_activation_email
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from .models import *


#Signal to send email for login by email_token
# @receiver(post_save , sender = User)
# def send_email_token(sender , instance , created , **kwargs):
#     try:
#         if created:
#             email_token = str(uuid.uuid4())
#             Profile.objects.create(user=instance , email_token = email_token)
#             email = instance.email
#             send_account_activation_email(email , email_token)
            
#     except Exception as e:
#         print(e)
