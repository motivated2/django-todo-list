from django.urls import path

from todo_list import views
from todo_list.views import TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", views.index, name="index"),
    path("create-task/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete")
]

app_name = "todo_list"
