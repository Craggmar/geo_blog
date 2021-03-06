# Generated by Django 4.0.3 on 2022-03-28 12:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='title',
            field=models.CharField(default='newtopic', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='topic',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
