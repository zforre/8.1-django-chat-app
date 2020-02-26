from django.urls import path

from . import views

app_name= 'chat'

urlpatterns = [
   path('<int:pk>/comments/add/', views.CommentCreateView.as_view(), name='comment_create'),
    path('add/', views.ChatCreateView.as_view(), name='chat_create'),
    path('<int:pk>/', views.ChatDetailView.as_view(), name='chat_detail'),
   path('', views.ChatListView.as_view(), name='chat_list') 
]

