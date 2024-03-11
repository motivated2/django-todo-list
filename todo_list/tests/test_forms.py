from django.test import TestCase
from todo_list.forms import TaskForm
from todo_list.models import Tag


class FormTests(TestCase):
    def test_task_form_valid_data(self):
        Tag.objects.create(name="NewTag")
        form = TaskForm(
            data={
                "content": "Test Task",
                "tags": Tag.objects.all()
            }
        )
        self.assertTrue(form.is_valid())

    def test_task_form_invalid_data(self):
        form = TaskForm(
            data={
                "content": "Test Task",
            }
        )
        self.assertFalse(form.is_valid())
