import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class AuthorsProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str___(self):
        return self.user.username


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    blog_post = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(
        AuthorsProfileInfo, on_delete=models.SET_NULL, null=True
    )
    image = models.ImageField(upload_to='blog_pics', blank=True, null=True)

    def __str__(self):
        return self.title

    def was_published(self):
        return timezone.now(
        ) - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()

    @property
    def number_of_comments(self):
        return BlogComment.objects.filter(blogpost=self).count()


class BlogComment(models.Model):
    blogpost = models.ForeignKey(
        BlogPost, related_name='comment', on_delete=models.CASCADE
    )
    author = models.ForeignKey(AuthorsProfileInfo, on_delete=models.CASCADE)
    comment = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.author) + ', ' + self.blogpost.title
