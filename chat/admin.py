from django.contrib import admin

# Register your models here.
from .models import Chat, Comment

admin.site.register(Chat)
admin.site.register(Comment)