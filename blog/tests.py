import sys
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from blog.models import Post


class BlogTest(TestCase):
    user_name = "testUser"
    email_address = "testmail.gmail.com"
    user_password = "191Pass"
    blog_title = "Good Test Title"
    blog_body = "Nice Body"

    def setUp(self):
        self.user = get_user_model().objects.create_user(username=self.user_name, email=self.email_address,
                                                         password=self.user_password)

        self.post = Post.objects.create(
            title=self.blog_title,
            body=self.blog_body,
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title=self.blog_title)
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', self.blog_title)
        self.assertEqual(f'{self.post.author}', self.user_name)
        self.assertEqual(f'{self.post.body}', self.blog_body)

    def test_post_list_view(self):
        response = self.client.get(reverse('blog_home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.blog_body)
        self.assertTemplateUsed(response, 'blog_home.html')

    def test_post_detail_views(self):
        # response = self.client.get(f"post/{self.post.pk}/") #Replaced with reverse url below
        url = reverse('post_detail', kwargs={'pk': self.post.pk})
        response = self.client.get(url)
        no_response = self.client.get('post/180000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, self.blog_title)
        self.assertContains(response, self.blog_body)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_create_view(self):  # new
        response = self.client.post(reverse('post_new'), {
            'title': self.blog_title,
            'body': self.blog_body,
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, self.blog_title)
        self.assertEqual(Post.objects.last().body, self.blog_body)

    def test_post_update_view(self):  # new
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })

        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):  # new
        response = self.client.post(
            reverse('post_delete', args='1'))

        self.assertEqual(response.status_code, 302)
