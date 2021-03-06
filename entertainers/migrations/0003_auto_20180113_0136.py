# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainers', '0002_auto_20180113_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainer',
            name='image1',
            field=models.ImageField(blank=True, default='no_image.png', null=True, upload_to='img1/'),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='image2',
            field=models.ImageField(blank=True, default='no_image.png', null=True, upload_to='img2/'),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='image3',
            field=models.ImageField(blank=True, default='no_image.png', null=True, upload_to='img3/'),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='image4',
            field=models.ImageField(blank=True, default='no_image.png', null=True, upload_to='img4/'),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='image5',
            field=models.ImageField(blank=True, default='no_image.png', null=True, upload_to='img5/'),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='profile_image',
            field=models.ImageField(blank=True, default='no_image.png', null=True, upload_to='profile/'),
        ),
    ]
