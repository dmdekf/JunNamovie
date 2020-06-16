# Generated by Django 2.1.15 on 2020-06-16 02:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('type', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('popularity', models.FloatField(default=0)),
                ('release', models.DateField(blank=True)),
                ('poster_URL', models.URLField(blank=True, default='')),
                ('backdrop_URL', models.URLField(blank=True, default='')),
                ('adult', models.BooleanField()),
                ('overview', models.TextField()),
                ('runtime', models.IntegerField(default=0)),
                ('status', models.BooleanField()),
                ('tagline', models.CharField(max_length=200)),
                ('vote_aver', models.FloatField(blank=True)),
                ('vote_count', models.IntegerField(blank=True)),
                ('genres', models.TextField()),
                ('gen', models.ManyToManyField(blank=True, related_name='movies', to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_movie_genre', models.CharField(max_length=45)),
                ('recommend_genre', models.ManyToManyField(related_name='recommends', to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(blank=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_score', to='movies.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_score', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
