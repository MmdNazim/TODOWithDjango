from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=65)  
    created_at = models.DateTimeField(auto_now_add=True)


class SubCategory(models.Model):
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)     #[NOTE: eikhane database relation krse, eita hoilo "one to one relationship"]
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='tasks')  #[NOTE: eikhane database relation krse, eita hoilo "one to many relationship" ||Ar eikhane "related_name='tasks'" dewa hoy jate kre kono prokar conflict na hoy amra easily access krte pari oi related_name ta dhore]
    subcategory = models.ManyToManyField(SubCategory, related_name='tasks')      #[NOTE: eikhane database relation krse, eita hoilo "many to many relationship"]
    title = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)        #[NOTE: eikhane "auto_now_add" ei function tar kaj holo je jokhn ami data entry krbo tokhn ei function ta current time ta nibe.]
    update_at = models.DateTimeField(auto_now=True)






