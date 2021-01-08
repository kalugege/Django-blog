from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title + ' ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')

    def short_content(self):
        return " ".join(self.content.split(' ')[:50])


class Comments(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)    
    name = models.CharField(max_length=10)
    comment = models.TextField(max_length=100)        

