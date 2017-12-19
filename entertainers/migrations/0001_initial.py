# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 10:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entertainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('description', models.CharField(choices=[('Band', 'Band'), ('Solo', 'Solo'), ('Comedian', 'Commedian'), ("Children's Entertainer", "Children's Entertainer")], default='Band', max_length=14)),
                ('genre', models.CharField(choices=[('Rock', 'Rock'), ('Metal', 'Metal'), ('Punk', 'Punk'), ('Blues', 'Blues'), ('Jazz', 'Jazz'), ('Classical', 'Classical'), ('Reggae', 'Reggae'), ('Ska', 'Ska'), ('Dance', 'Dance'), ('Electronic', 'Electronic'), ('Folk', 'Folk'), ('Pop', 'Pop'), ('Funk', 'Funk'), ('Trad', 'Trad'), ('Country', 'Country'), ('Soul', 'Soul'), ('RnB', 'RnB'), ('Other', 'Other')], default='Rock', max_length=11)),
                ('location', models.CharField(choices=[('Antrim', 'Antrim'), ('Armagh', 'Armagh'), ('Carlow', 'Carlow'), ('Cavan', 'Cavan'), ('Clare', 'Clare'), ('Cork', 'Cork'), ('Derry', 'Derry'), ('Donegal', 'Donegal'), ('Down', 'Down'), ('Dublin', 'Dublin'), ('Fermanagh', 'Fermanagh'), ('Galway', 'Galway'), ('Kerry', 'Kerry'), ('Kildare', 'Kildare'), ('Kilkenny', 'Kilkenny'), ('Laois', 'Laois'), ('Leitrim', 'Leitrim'), ('Limerick', 'Limerick'), ('Longford', 'Longford'), ('Louth', 'Louth'), ('Mayo', 'Mayo'), ('Meath', 'Meath'), ('Monaghan', 'Monaghan'), ('Offaly', 'Offaly'), ('Roscommon', 'Roscommon'), ('Sligo', 'Sligo'), ('Tipperary', 'Tipperary'), ('Tyrone', 'Tyrone'), ('Waterford', 'Waterford'), ('Westmeath', 'Westmeath'), ('Wexford', 'Wexford'), ('Wicklow', 'Wicklow')], default='Antrim', max_length=10)),
                ('profile_image', models.ImageField(default='media/no_image.png', upload_to='media/profile/%Y/%m/%d')),
                ('image1', models.ImageField(default='media/no_image.png', upload_to='media/img1/%Y/%m/%d')),
                ('image2', models.ImageField(default='media/no_image.png', upload_to='media/img2/%Y/%m/%d')),
                ('image3', models.ImageField(default='media/no_image.png', upload_to='media/img3/%Y/%m/%d')),
                ('image4', models.ImageField(default='media/no_image.png', upload_to='media/img4/%Y/%m/%d')),
                ('image5', models.ImageField(default='media/no_image.png', upload_to='media/img5/%Y/%m/%d')),
                ('language', multiselectfield.db.fields.MultiSelectField(choices=[('English', 'English'), ('Irish', 'Irish'), ('French', 'French'), ('Spanish', 'Spanish'), ('German', 'German')], default='English', max_length=35)),
                ('music', multiselectfield.db.fields.MultiSelectField(choices=[('Original', 'Original'), ('Covers', 'Covers'), ('Comedy', 'Comedy'), ('Parody', 'Parody')], default='Originals', max_length=29)),
                ('gig_length_from', models.CharField(choices=[('60', '60'), ('90', '90'), ('120', '120'), ('180', '180'), ('240', '240')], default=60, max_length=3)),
                ('gig_length_to', models.CharField(choices=[('60', '60'), ('90', '90'), ('120', '120'), ('180', '180'), ('240', '240')], default=90, max_length=3)),
                ('bio', models.TextField()),
                ('set_list', models.TextField(default='Available on Request.')),
                ('influences', models.TextField(default='All Genres and decades.')),
                ('set_up_requirements', multiselectfield.db.fields.MultiSelectField(choices=[('Power Source', 'Power Source'), ('Stage Cover - If Outside', 'Stage Cover - If Outside'), ('Accomodation', 'Accomodation'), ('Food', 'Food'), ('Beverages', 'Beverages')], default='Power Source', max_length=65)),
                ('travel_distance', models.CharField(choices=[('same county', 'same county'), ('same province', 'same province'), ('nationwide', 'nationwide')], default='nationwide', max_length=13)),
                ('min_price', models.CharField(choices=[('100', '100'), ('200', '200'), ('300', '300'), ('400', '400'), ('500', '500'), ('600', '600'), ('700', '700'), ('800', '800'), ('900', '900'), ('1000', '1000'), ('1100', '1100'), ('1200', '1200'), ('1300', '1300'), ('1400', '1400'), ('1500', '1500'), ('1600', '1600'), ('1700', '1700'), ('1800', '1800'), ('1900', '1900'), ('2000', '2000'), ('2100', '2100'), ('2200', '2200'), ('2300', '2300'), ('2400', '2400'), ('2500', '2500')], default='100', max_length=4)),
                ('max_price', models.CharField(choices=[('100', '100'), ('200', '200'), ('300', '300'), ('400', '400'), ('500', '500'), ('600', '600'), ('700', '700'), ('800', '800'), ('900', '900'), ('1000', '1000'), ('1100', '1100'), ('1200', '1200'), ('1300', '1300'), ('1400', '1400'), ('1500', '1500'), ('1600', '1600'), ('1700', '1700'), ('1800', '1800'), ('1900', '1900'), ('2000', '2000'), ('2100', '2100'), ('2200', '2200'), ('2300', '2300'), ('2400', '2400'), ('2500', '2500')], default='500', max_length=4)),
                ('soundcloud_audio', models.TextField(default='<iframe width="100%" height="300" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/209382959&amp;color=%23ff5500&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;show_teaser=true&amp;visual=true"></iframe>')),
                ('youtube_video', models.TextField(default='<iframe width="560" height="315" src="https://www.youtube.com/embed/xaE2wV-HMxs" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>')),
                ('likes_total', models.IntegerField(default=1)),
                ('dislikes_total', models.IntegerField(default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
