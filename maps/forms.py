from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Riot

class RegisterUser(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(RegisterUser,self).__init__(*args,**kwargs)
        for fieldname in ['username','email','password1','password2']:
            self.fields[fieldname].help_text=None
            
    email=forms.EmailField()
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UpdateUser(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']

class UpdateProfile(forms.ModelForm):
    class Meta:
         model=Profile
        fields=['contact','location','bio','image']
        
        
        
class PostRiot(forms.ModelForm):
    class Meta:
        model=Project
        fields=['name','description','location','address','city']
        

