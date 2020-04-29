from django.db import models

# Create your models here.
class Contact(models.Model):
    S_No = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Phone=models.CharField(max_length=15)
    Content=models.CharField(max_length=300)
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return self.Name