# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainers', '0023_auto_20171123_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='entertainer',
            name='profile_image',
            field=models.ImageField(default='media/no_image.png', upload_to='media/profile/'),
        ),
    ]
