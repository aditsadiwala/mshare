# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0016_music_likenum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='likenum',
            field=models.IntegerField(default=0),
        ),
    ]
