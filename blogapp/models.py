from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        print(self.text[:40]+'...')


class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=600,default='')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    image = models.ImageField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

