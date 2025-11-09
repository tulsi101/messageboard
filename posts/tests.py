# posts/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostTests(TestCase):
    def setUp(self):
        Post.objects.create(title="Hello", body="World")

    def test_list_view_status_code(self):
        resp = self.client.get(reverse("post_list"))
        self.assertEqual(resp.status_code, 200)

    def test_detail_view_status_code(self):
        post = Post.objects.first()
        resp = self.client.get(reverse("post_detail", args=[post.id]))
        self.assertEqual(resp.status_code, 200)
