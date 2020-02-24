from django.shortcuts import render
from django.views import generic
from .models import Chat
from django.urls import reverse
from django.urls import reverse_lazy

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'chat/index.html'
    model = Chat
