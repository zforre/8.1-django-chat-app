from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from .models import Profile
from .forms import CustomUserCreationForm

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProfileCreateView(generic.CreateView):
    model = Profile
    success_url = reverse_lazy('chats:chat_list')
    fields = ('location', 'avatar')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileDetailView(generic.DetailView):
    model = Profile
