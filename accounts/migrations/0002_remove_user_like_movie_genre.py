# Generated by Django 2.1.15 on 2020-06-16 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='like_movie_genre',
        ),
    ]
