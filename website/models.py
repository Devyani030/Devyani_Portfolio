from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.name
    
STATUS ={
    (0,'Draft'),
    (1,'Publish')
}
    
class Blogs(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author= models.CharField(max_length=20)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title