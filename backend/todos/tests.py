from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(title="first todo", body="a body here")

    def test_title_content(self):
        # Use the created instance to test
        expected_object_name = f"{self.todo.title}"
        self.assertEqual(expected_object_name, "first todo")

    def test_body_content(self):
        # Use the created instance to test
        expected_object_name = f"{self.todo.body}"
        self.assertEqual(expected_object_name, "a body here")
