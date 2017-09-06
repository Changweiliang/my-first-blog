from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    published_date= models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return self.title

class PostComment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=50)
    comment_text = models.TextField()
    comment_published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.comment_text