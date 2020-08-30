from django.db import models

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