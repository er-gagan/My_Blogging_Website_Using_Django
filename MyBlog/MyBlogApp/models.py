from django.db import models

# Create your models here.
class Post(models.Model):
    S_No = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    Content = models.TextField()
    Author = models.CharField(max_length=100)
    slug = models.CharField(max_length=200)
    TimeStamp = models.DateTimeField(blank=True)
    
    def __str__(self):
        return self.Title