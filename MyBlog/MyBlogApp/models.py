from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
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
    
class BlogComment(models.Model):
    S_No = models.AutoField(primary_key=True)
    comment = models.TextField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    BlogPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    Parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    TimeStamp = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.comment[0:13]+"..."+" by "+self.User.username
    