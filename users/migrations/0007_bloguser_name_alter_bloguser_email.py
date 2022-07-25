# Generated by Django 4.0.4 on 2022-07-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_bloguser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='bloguser',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]