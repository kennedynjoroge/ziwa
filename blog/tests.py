import sys
# import django
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from blog.models import Post
#
# sys.path.append("./")
# django.setup()


class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testUser", email="testmail.gmail.com",
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
        # response = self.client.get(f"post/{self.post.pk}/") #Replaced with reverse url below
        url = reverse('post_detail', kwargs={'pk': self.post.pk})
        response = self.client.get(url)
        no_response = self.client.get('post/180000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Good Test Title')
        self.assertContains(response, 'Nice Body')
        self.assertTemplateUsed(response, 'post_detail.html')