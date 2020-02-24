from django.db import models
from django.urls import reverse

# Create your models here.
class Chat(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('Member', related_name='chat')

    def __str__(self):
        return self.name[:50]

    def get_absolute_url(self):
        return reverse('chat:index')
    
class Member(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name[:50]