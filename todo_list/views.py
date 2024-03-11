from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from todo_list.forms import TaskForm
from todo_list.models import Task, Tag


def index(request):
    tasks = Task.objects.prefetch_related("tags")
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


def toggle_task_is_done(request, pk):
    task = Task.objects.get(id=pk)
    if task.is_done:
        task.is_done = False
    else:
        task.is_done = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo_list:index"))


class TagListView(ListView):
    model = Tag
    success_url = reverse_lazy("todo_list:")
