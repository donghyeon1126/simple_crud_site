from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=10)
    author_password = models.TextField()

class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment_content = models.TextField()
    comment_date = models.DateTimeField()
    author = models.CharField(max_length=10)
    author_password = models.TextField()