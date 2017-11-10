# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20170919_2300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-date_comment']},
        ),
        migrations.AlterModelOptions(
            name='music',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='music',
            name='public',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='music',
            name='songupload',
            field=models.FileField( upload_to=''),

        ),
        migrations.AddField(
            model_name='music',
            name='timestamp',
            field=models.DateField(auto_now_add=True),

        ),
        migrations.AlterField(
            model_name='music',
            name='songphoto',
            field=models.FileField(upload_to=''),
        ),
    ]
