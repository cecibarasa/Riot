from django import forms
from .models import Profile,Riot

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
        

