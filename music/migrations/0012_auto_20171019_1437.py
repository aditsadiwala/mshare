# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 09:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20171019_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
