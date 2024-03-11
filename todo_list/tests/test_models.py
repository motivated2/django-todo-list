from django.test import TestCase
from django.utils import timezone
from todo_list.models import Task, Tag


class TaskModelTest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="Tag1")
        self.tag2 = Tag.objects.create(name="Tag2")
        self.task1 = Task.objects.create(
            content="Task 1",
            deadline=timezone.now(),
        )
        self.task1.tags.add(self.tag1)
        self.task1.tags.add(self.tag2)

    def test_task_creation(self):
        self.assertEqual(self.task1.content, "Task 1")
        self.assertTrue(self.task1.deadline)
        self.assertFalse(self.task1.is_done)

    def test_task_str_representation(self):
        self.assertEqual(str(self.task1), "Task 1 False")

    def test_task_tags(self):
        self.assertEqual(self.task1.tags.count(), 2)
        self.assertIn(self.tag1, self.task1.tags.all())
        self.assertIn(self.tag2, self.task1.tags.all())


class TagModelTest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="Tag1")
        self.tag2 = Tag.objects.create(name="Tag2")

    def test_tag_creation(self):
        self.assertEqual(self.tag1.name, "Tag1")
        self.assertEqual(self.tag2.name, "Tag2")

    def test_tag_str_representation(self):
        self.assertEqual(str(self.tag1), "Tag1")
        self.assertEqual(str(self.tag2), "Tag2")
