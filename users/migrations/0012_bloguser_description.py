# Generated by Django 4.0.3 on 2022-08-02 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_bloguser_permission_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='description',
            field=models.CharField(default='Napisz coś o sobie...', max_length=100),
        ),
    ]
