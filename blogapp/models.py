from django.db import models
from django.contrib.auth.models import User
import PIL.Image

def images_path(instance, filename):
    return "{}/{}".format(instance.topic.title, filename)

def topic_images_path(self, filename):
    return "{}/{}".format(self.title, filename)

class Topic(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=400)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    header_image = models.ImageField(null=True, default='_defaults/default_topic_image.png', upload_to=topic_images_path)
    confirmed = models.BooleanField(default=False)


    
    def __str__(self):
        return self.title.capitalize()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = PIL.Image.open(self.header_image.path)

        output_size = (1600, 768)
        new_img= img.resize(output_size)
        new_img.save(self.header_image.path)

class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=600)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=images_path)
    show_in_gallery = models.BooleanField(default=True)



