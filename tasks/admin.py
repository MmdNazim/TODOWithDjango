from django.contrib import admin
from .models import Task

#using decorator:
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title","completed", "created_at", "update_at")
    search_fields = ("title",)    #[NOTE: tuples use krle ekta field hoile oi fielder last e must comma(,) dite hbe but list use krle ekta fielder last e comma(,) dite hoy na "search_fields =["title"]"]
