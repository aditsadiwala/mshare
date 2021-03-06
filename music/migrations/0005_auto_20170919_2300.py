# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 17:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0004_user1'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('date_comment', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songname', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=30)),
                ('songformat', models.CharField(max_length=10)),
                ('songphoto', models.CharField(max_length=1000)),
                ('likes', models.IntegerField(default=0)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('emailid', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('no_followers', models.IntegerField(default=0)),
                ('no_following', models.IntegerField(default=0)),
                ('prefferedgenre', models.CharField(max_length=20)),
                ('followers', models.TextField(blank=True)),
                ('followingd', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.DeleteModel(
            name='User1',
        ),
        migrations.DeleteModel(
            name='album',
        ),
        migrations.DeleteModel(
            name='song',
        ),
        migrations.AddField(
            model_name='comments',
            name='song_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.music'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
