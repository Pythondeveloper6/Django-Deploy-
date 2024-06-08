from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from utils.generate_code import generate_code

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/')
    code = models.CharField(max_length=20,default=generate_code)
    
    def __str__(self):
        return str(self.user)


'''
    sender : user 
    instance : new user : data : email , username
    created: true :flase
'''


@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):   # reciever 
    if created : # new user : signup not edit
        Profile.objects.create(
            user=instance
        )



PHONE_TYPE = (
    ('Primary' , 'Primary') , 
    ('Secondary' , 'Secondary') , 
)


class Phones(models.Model):
    user = models.ForeignKey(User,related_name='user_phone',on_delete=models.CASCADE)
    type = models.CharField(max_length=20,choices=PHONE_TYPE)
    number = models.CharField(max_length=25)
    
    def __str__(self):
        return str(self.user)




ADDRESS_TYPE = (
    ('Home' , 'Home') , 
    ('Office' , 'Office') , 
    ('Bussines' , 'Bussines') , 
    ('Other' , 'Other') , 
)


class Address(models.Model):
    user = models.ForeignKey(User,related_name='user_address',on_delete=models.CASCADE)
    address = models.TextField(max_length=300)
    type = models.CharField(max_length=20,choices=ADDRESS_TYPE)
    
    def __str__(self):
        return self.address




