# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "blog_home.html"
    context_object_name = "blog_posts_list"  # replace object_list in html


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = "blog_post_detail"


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

    # success_url = reverse_lazy("post_detail")

    def test_func(self):  # Check if logged in user is the post creator before allowing update/delete
        obj = self.get_object()
        print("Object author: ", obj.author, " User ", self.request.user)
        return obj.author == self.request.user


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("blog_home")

    def test_func(self):  # Check if logged in user is the post creator before allowing update/delete
        obj = self.get_object()

        return obj.author == self.request.user
