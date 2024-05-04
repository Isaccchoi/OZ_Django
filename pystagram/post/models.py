import re

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from utils.models import TimestampModel

User = get_user_model()


class Post(TimestampModel):
    content = models.TextField('본문')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.user}] post'

    class Meta:
        verbose_name = '포스트'
        verbose_name_plural = '포스트 목록'


class PostImage(TimestampModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('이미지', upload_to='post/%Y/%m/%d')

    def __str__(self):
        return f'{self.post} image'

    class Meta:
        verbose_name = '이미지'
        verbose_name_plural = '이미지 목록'


# Post
    # 이미지(여러개)
    # 글
    # 작성자
    # 작성일자
    # 수정일자

# 태그 N:N
class Tag(TimestampModel):
    tag = models.CharField('태그', max_length=100, unique=True)
    posts = models.ManyToManyField(Post, related_name='tags')

    def __str__(self):
        return self.tag


# 댓글
class Comment(TimestampModel):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField('내용', max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'[comment]{self.post} | {self.user}'


class Like(TimestampModel):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f'[like] {self.post} | {self.user}'


@receiver(post_save, sender=Post)
def post_post_save(sender, instance, created, **kwargs):
    hashtags = re.findall(r'#(\w{1,100})(?=\s|$)', instance.content)

    instance.tags.clear()

    if hashtags:
        tags = [
            Tag.objects.get_or_create(tag=hashtag)
            for hashtag in hashtags
        ]
        tags = [tag for tag, _ in tags]

        instance.tags.add(*tags)
