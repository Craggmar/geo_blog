# Generated by Django 4.0.4 on 2022-07-19 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0019_image_show_in_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.CharField(max_length=400),
        ),
    ]
