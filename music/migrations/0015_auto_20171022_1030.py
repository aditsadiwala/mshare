# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 05:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0014_remove_music_songformat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='music',
            options={'ordering': ['timestamp']},
        ),
    ]
