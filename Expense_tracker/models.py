from django.db import models
import datetime as dt

# Create your models here.
class User(models.Model):
    user_email = models.EmailField(max_length=254,primary_key=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s, %s'%(self.first_name,self.last_name,self.user_email)
    def to_dict(self):
        user_dict = {'user_email': self.user_email,
                    'first_name': self.first_name,
                    'last_name':self.last_name}
        return user_dict
class Income(models.Model):
    user_email = models.ForeignKey("User", on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    isPeriodic = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        d = self.date
        return '%d, %s, saved on: %d.%d.%d %d:%d'%(self.amount,'Periodic' if(self.isPeriodic) else 'non-Periodic', d.day, d.month, d.year, d.hour, d.minute)    
class Outcome(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    isPeriodic = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        d = self.date
        return '%d, %s, saved on: %d.%d.%d %d:%d'%(self.amount,'Periodic' if(self.isPeriodic) else 'non-Periodic', d.day, d.month, d.year, d.hour, d.minute) 