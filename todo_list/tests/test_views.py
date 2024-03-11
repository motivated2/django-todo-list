from django.http import HttpResponseRedirect
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.utils import timezone
from todo_list.views import (
    index,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_task_is_done,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)
from todo_list.models import Task, Tag


class ViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(
            content="Test Task",
            deadline=timezone.now()
        )

    def test_index_view(self):
        request = self.factory.get(reverse("todo_list:index"))
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_task_create_view(self):
        request = self.factory.get(reverse("todo_list:task-create"))
        response = TaskCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_task_update_view(self):
        request = self.factory.get(
            reverse(
                "todo_list:task-update",
                kwargs={"pk": self.task.pk}
            )
        )
        response = TaskUpdateView.as_view()(request, pk=self.task.pk)
        self.assertEqual(response.status_code, 200)

    def test_task_delete_view(self):
        request = self.factory.get(
            reverse(
                "todo_list:task-delete",
                kwargs={"pk": self.task.pk}
            )
        )
        response = TaskDeleteView.as_view()(request, pk=self.task.pk)
        self.assertEqual(response.status_code, 200)

    def test_toggle_task_is_done_view(self):
        request = self.factory.get(
            reverse(
                "todo_list:toggle-task-is-done",
                kwargs={"pk": self.task.pk}
            )
        )
        response = toggle_task_is_done(request, pk=self.task.pk)
        self.assertIsInstance(response, HttpResponseRedirect)

    def test_tag_list_view(self):
        request = self.factory.get(reverse("todo_list:tag-list"))
        response = TagListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_tag_create_view(self):
        request = self.factory.get(reverse("todo_list:tag-create"))
        response = TagCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_tag_update_view(self):
        request = self.factory.get(
            reverse(
                "todo_list:tag-update",
                kwargs={"pk": self.tag.pk}
            )
        )
        response = TagUpdateView.as_view()(request, pk=self.tag.pk)
        self.assertEqual(response.status_code, 200)

    def test_tag_delete_view(self):
        request = self.factory.get(
            reverse(
                "todo_list:tag-delete",
                kwargs={"pk": self.tag.pk}
            )
        )
        response = TagDeleteView.as_view()(request, pk=self.tag.pk)
        self.assertEqual(response.status_code, 200)
