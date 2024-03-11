from django.urls import path

from todo_list import views
from todo_list.views import TaskCreateView

urlpatterns = [
    path("", views.index, name="index"),
    path("create-task/", TaskCreateView.as_view(), name="task-create")
]

app_name = "todo_list"
