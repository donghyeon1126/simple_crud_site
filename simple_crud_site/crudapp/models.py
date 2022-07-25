from django.db import models
class Posts(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=10)
    author_password = models.TextField()