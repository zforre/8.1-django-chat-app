from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Chat(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    members = models.ManyToManyField(User)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chat:chat_detail', args=(self.id,))
    
class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:50]

    def get_absolute_url(self):
        return reverse('chat:chat_detail', args=(self.chat_id,))