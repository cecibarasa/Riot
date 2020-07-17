from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.gis.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_pic')
    phone_number = models.CharField(max_length = 10,blank =True)
    bio = models.TextField(blank=True)
   
    
    def __str__(self):
        return self.user

class Maps(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)   
    street= models.CharField(max_length=50)     
