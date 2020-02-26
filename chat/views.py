from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Chat, Comment
# Create your views here.

class ChatCreateView(generic.CreateView): 
    model = Chat
    fields= ('name', 'description')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        # return super().form_valid(form)
        self.object = form.save()
        self.object.members.add(self.request.user)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ChatDetailView(generic.DetailView):
    model = Chat

class ChatListView(generic.ListView):
    # will look for template named chat_list.html by default
    model = Chat

class CommentCreateView(generic.CreateView):
    model = Comment
    fields = ('text',)

    def form_valid(self,form):
        form.instance.user = self.request.user
        form.instance.chat_id = self.kwargs['pk']
        return super().form_valid(form)
