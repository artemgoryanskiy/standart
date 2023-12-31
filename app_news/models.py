from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class CategoryNews(models.Model):
    TITLE_CHOICES = (
        ('news', 'Новости'),
        ('ads', 'Реклама'),
    )
    title = models.CharField(max_length=250, choices=TITLE_CHOICES, default='news')
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.title


class PostNews(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_img/', blank=True, null=True)
    body = models.TextField()
    category = models.ForeignKey(CategoryNews, on_delete=models.CASCADE, blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(PostNews, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


