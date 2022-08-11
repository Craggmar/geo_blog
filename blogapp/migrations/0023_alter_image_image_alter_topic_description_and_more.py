# Generated by Django 4.1 on 2022-08-09 11:10

import blogapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0022_alter_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=blogapp.models.images_path),
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='topic',
            name='header_image',
            field=models.ImageField(default='_defaults/default_topic_image.png', null=True, upload_to=blogapp.models.topic_images_path),
        ),
    ]
