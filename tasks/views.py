from django.shortcuts import render

from.models import Task

# Create your views here.
# crud = create, read, update, delete
#NOTE: create equivalent to = Post, read = get, update = put/patch, delete ----> this all are use in rest api's.

def task_list(request):
    tasks = Task.objects.all()
    return render(
        request, 
        "tasks/base.html",
        {"tasks": tasks}
    )

