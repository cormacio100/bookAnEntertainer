# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-19 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainers', '0008_auto_20180219_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainer',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='image1/'),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
