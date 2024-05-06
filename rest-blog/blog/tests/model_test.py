from datetime import timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from blog.models import Blog


class BlogModelTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='test',
            is_active=True
        )

        Blog.objects.create(
            title='배포',
            content='본문',
            author=user,
        )

        future_published_at = timezone.now() + timedelta(days=30)

        Blog.objects.create(
            title='아직 배포 안됨',
            content='본문',
            author=user,
            published_at=future_published_at
        )

    def test_blog_is_published(self):
        published_blog = Blog.objects.get(title='배포')
        unpublished_blog = Blog.all_objects.get(title='아직 배포 안됨')

        self.assertEqual(published_blog.is_active, True)
        self.assertEqual(unpublished_blog.is_active, False)

    def test_blog_manager(self):
        objects_count = Blog.objects.count()
        all_objects_count = Blog.all_objects.count()

        self.assertEqual(objects_count, 1)
        self.assertEqual(all_objects_count, 2)
