from django.urls import path

from.views import task_list
from.views import post_list

urlpatterns = [
    path('task_list', task_list, name='task_list'), 
    path('post', post_list), 
]
