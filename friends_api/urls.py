from django.urls import path
from .views import friend_list

urlpatterns = [
    path('', friend_list, name='friend-list'),
]