from django.db import models
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.

class Riot(model.Models):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField()
    location=models.PointField()
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    posted=models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='media/',default='default.png')
    bio=models.TextField(blank=True)
    contact=models.CharField(max_length=30, blank=True)
    location=models.CharField(max_length=50, blank=True)
    company=models.CharField(max_length=50, blank=True)      

    def __str__(self):
        return self.user.username

    def save(self,*args,**kwargs):
        super().save()
        
        img=Image.open(self.image.path)
        
        if img.height>400 and img.width>400:
            size=(400,400)
            img.thumbnail(size)
            img.save(self.image.path)     