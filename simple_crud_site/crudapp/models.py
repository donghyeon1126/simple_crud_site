from django.db import models
class Posts(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=10)
    content = models.TextField()
    date = models.DateTimeField()