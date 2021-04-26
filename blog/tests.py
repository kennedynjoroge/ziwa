import sys
sys.path.append("./")
import django
django.setup()

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from blog.models import Post


class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testUser", email="testemail.gmail.com",
                                                         password="Password")

        self.post = Post.objects.create(
            title="Good Test Title",
            body="Nice Body",
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title="A simple title")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Good Test Title')
        self.assertEqual(f'{self.post.author}', 'testUser')
        self.assertEqual(f'{self.post.body}', 'Nice Body')

    def test_post_list_view(self):
        response = self.client.get(reverse('blog_home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice Body')
        self.assertTemplateUsed(response, 'blog_home.html')

    def test_post_detail_views(self):
        response = self.client.get("post/1")
        no_response = self.client.get('post/180000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertEqual(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')


    def test_post_edit_view(self):
        response = self.client.get("post/1/edit")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice Body')
        self.assertTemplateUsed(response, 'blog_home.html')
