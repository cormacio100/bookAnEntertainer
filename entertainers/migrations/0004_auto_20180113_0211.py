# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 02:11
from __future__ import unicode_literals

from django.db import migrations, models
import entertainers.models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainers', '0003_auto_20180113_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainer',
            name='image1',
            field=models.ImageField(blank=True, default='no_image.png', null=True, upload_to=entertainers.models.img1_image_path),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='image2',
            field=models.ImageField(blank=True, default='no_image.png', null=True, upload_to=entertainers.models.img2_image_path),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='image3',
            field=models.ImageField(blank=True, default='no_image.png', null=True, upload_to=entertainers.models.img3_image_path),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='image4',
            field=models.ImageField(blank=True, default='no_image.png', null=True, upload_to=entertainers.models.img4_image_path),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='image5',
            field=models.ImageField(blank=True, default='no_image.png', null=True, upload_to=entertainers.models.img5_image_path),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='profile_image',
            field=models.ImageField(blank=True, default='no_image.png', null=True, upload_to=entertainers.models.profile_image_path),
        ),
    ]
