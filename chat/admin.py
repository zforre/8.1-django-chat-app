from django.contrib import admin

# Register your models here.
from .models import Chat, Member

admin.site.register(Chat)
admin.site.register(Member)