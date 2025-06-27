from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)
    
    def __str__(self):
        return self.top_name
    
    
    
class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name



class UserProfile(models.Model):
    webpage = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    username = models.CharField(max_length = 100)
    email = models.EmailField(max_length=254)
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.username} | {self.webpage}"