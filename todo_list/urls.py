from django.urls import path

from todo_list import views

urlpatterns = [
    path("", views.index, name="index")
]

app_name = "todo_list"
