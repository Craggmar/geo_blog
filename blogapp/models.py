from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    pass
