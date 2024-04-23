from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from utils.models import TimestampModel

User = get_user_model()


class Blog(TimestampModel):
    CATEGORY_CHOICES = (
        ('free', '자유'),
        ('travel', '여행'),
        ('cat', '고양이'),
        ('dog', '강아지'),
    )
    category = models.CharField('카테고리', max_length=10, choices=CATEGORY_CHOICES, default='free')
    title = models.CharField('제목', max_length=100)
    content = models.TextField('본문')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField('이미지', null=True, blank=True, upload_to='blog/%Y/%m/%d')
    # 2024/4/23일
    # blog/2024/4/23/이미지파일.jpg
    # ImageField, FieldField와 같지만 이미지만 업로드하게 되어있다.
    # varchar => 경로만 저장을 함

    # models.CASCADE => 같이 삭제
    # models.PROTECT => 삭제가 불가능함 (유저를 삭제하려고할때 블로그가 있으면 유저 삭제가 불가능)
    # models.SET_NULL => 널값을 넣습니다. => 유저 삭제시 블로그의 author가 null이 됨

    def __str__(self):
        return f'[{self.get_category_display()}] {self.title[:10]}'

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'blog_pk': self.pk})

    class Meta:
        verbose_name = '블로그'
        verbose_name_plural = '블로그 목록'

    # category update
    # Blog.objects.filter(category='').update(category='free')


# 제목
# 본문
# 작성일자
# 수정일자
# 카테고리

# 작성자 => 패스(추후 업데이트)


class Comment(TimestampModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.CharField('본문', max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.blog.title} 댓글'

    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = '댓글 목록'
        ordering = ('-created_at', '-id')

    # blog
    # 댓글 내용
    # 작성자
    # 작성일자
    # 수정일자
