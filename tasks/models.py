from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=65)
    created_at = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    title = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)        #[NOTE: eikhane "auto_now_add" ei function tar kaj holo je jokhn ami data entry krbo tokhn ei function ta current time ta nibe.]
    update_at = models.DateTimeField(auto_now=True)


class Blog(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)     
    update_at = models.DateTimeField(auto_now=True)




