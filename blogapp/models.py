from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

def topic_images_path(instance, filename):
    return "{}/{}".format(instance.topic.title, filename)

class Topic(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=400)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    header_image = models.ImageField(null=True, default='_defaults/default_topic_image.png')

    def __str__(self):
        return self.title.capitalize()

class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=600,default='')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=topic_images_path)
    show_in_gallery = models.BooleanField(default=True)


