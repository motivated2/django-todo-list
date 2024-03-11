from django.shortcuts import render

from todo_list.models import Task


def index(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks
    }

    return render(
        request,
        "todo_list/index.html",
        context=context
    )
