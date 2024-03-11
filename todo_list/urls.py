from django.urls import path

from todo_list import views
from todo_list.views import (
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_task_is_done,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)


urlpatterns = [
    path("", views.index, name="index"),
    path("create-task/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "<int:pk>/toggle-is-done",
        toggle_task_is_done,
        name="toggle-task-is-done"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list",
    ),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo_list"
