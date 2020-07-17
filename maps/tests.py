from django.test import TestCase
from .models import Riot
from django.contrib.auth.models import User

# Create your tests here.
class RiotTestClass(TestCase):
    def setup(self):
        self.user=User(username='jefferson')
        self.user.save()
        self.riot=Riot(user=self.user,name='test',description='this is test project')
        self.riot.save()


    #TEST METHOD    
    def test_save(self):
        self.riot.save_riot()
        riot=Riot.objects.all()
        self.assertTrue(len(riot)==1)
     
    #TEST DELETE METHOD   
    def test_delete(self):
        Riot.delete_riot(self.riot.pk)
        after_delete=Riot.objects.all()
        self.assertTrue(len(after_delete)==0)
        
    #TEST GET ELEMENT BY D
    def test_get_by_id(self):
        riot=Riot.get_riot(self.riot.id)
        self.assertEqual(riot.name,'test')    


