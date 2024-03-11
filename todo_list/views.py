from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from todo_list.forms import TaskForm
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


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("todo_list:index")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("todo_list:index")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:index")
