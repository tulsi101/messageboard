# posts/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"
    ordering = ["-created"]

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

class PostCreateView(CreateView):
    model = Post
    fields = ["title", "body"]
    template_name = "posts/post_form.html"

class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "body"]
    template_name = "posts/post_form.html"

class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

from django.contrib.auth import get_user_model
from django.http import HttpResponse


def create_admin(request):
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "Admin123")
        return HttpResponse("Superuser created: admin / Admin123")
    else:
        return HttpResponse("Superuser already exists.")