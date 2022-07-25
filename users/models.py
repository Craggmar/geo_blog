from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class BlogUser(models.Model):
    def user_profile_images_path(request, filename):
        return "users/{}/{}".format(request.user.username, filename)

    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)    
    email = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30, blank=True,)
    last_name = models.CharField(max_length=30, blank=True,)
    profile_picture = models.ImageField(blank=True, default='_defaults/default_user.png', upload_to = user_profile_images_path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_picture.path)

        if img.height or img.width > 300:
            output_size = (300,300)
            img.thumbnail (output_size)
            img.save(self.profile_picture.path)

    def __str__(self):
        return str(self.user)


    
    
    
    