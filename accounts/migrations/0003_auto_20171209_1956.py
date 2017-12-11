# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_entertainer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_entertainer',
        ),
        migrations.AddField(
            model_name='user',
            name='account_type',
            field=models.CharField(default='General', max_length=11),
        ),
    ]