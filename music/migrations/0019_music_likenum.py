# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0018_remove_music_likenum'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='likenum',
            field=models.IntegerField(default=0),
        ),
    ]
