# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainers', '0009_auto_20171122_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainer',
            name='gig_length_from',
            field=models.CharField(choices=[('60', '60'), ('90', '90'), ('120', '120'), ('180', '180'), ('240', '240')], default=60, max_length=3),
        ),
        migrations.AlterField(
            model_name='entertainer',
            name='gig_length_to',
            field=models.CharField(choices=[('60', '60'), ('90', '90'), ('120', '120'), ('180', '180'), ('240', '240')], default=90, max_length=3),
        ),
    ]