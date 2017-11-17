# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Entertainer(models.Model):

    #   DEFINE CHOICES LISTS WITH CONSTANTS
    ENT_TYPES = (
        ('BAND', 'Band'),
        ('SOLO_PERFORMER', 'Solo Performer')
    )
    GENRE_TYPES = (
        ('ROCK', 'Rock'),
        ('METAL', 'Metal'),
        ('PUNK', 'Punk'),
        ('BLUES', 'Blues'),
        ('JAZZ', 'Jazz'),
        ('CLASSICAL', 'Classical'),
        ('REGGAE', 'Reggae'),
        ('SKA', 'Ska'),
        ('DANCE', 'Dance'),
        ('FUNK', 'Funk'),
    )
    COUNTIES = (
        ('ANTRIM', 'Antrim'),
        ('ARMAGH', 'Armagh'),
        ('CARLOW', 'Carlow'),
        ('CAVAN', 'Cavan'),
        ('CLARE', 'Clare'),
        ('CORK', 'Cork'),
        ('DERRY', 'Derry'),
        ('DONEGAL', 'Donegal'),
        ('DOWN', 'Down'),
        ('DUBLIN', 'Dublin'),
        ('FERMANAGH', 'Fermanagh'),
        ('GALWAY', 'Galway'),
        ('KERRY', 'Kerry'),
        ('KILDARE', 'Kildare'),
        ('KILKENNY', 'Kilkenny'),
        ('LAOIS', 'Laois'),
        ('LEITRIM', 'Leitrim'),
        ('LIMERICK', 'Limerick'),
        ('LONGFORD', 'Longford'),
        ('LOUTH', 'Louth'),
        ('MAYO', 'Mayo'),
        ('MEATH', 'Meath'),
        ('MONAGHAN', 'Monaghan'),
        ('OFFALY', 'Offaly'),
        ('ROSCOMMON', 'Roscommon'),
        ('SLIGO', 'Sligo'),
        ('TIPPERARY', 'Tipperary'),
        ('TYRONE', 'Tyrone'),
        ('WATERFORD', 'Waterford'),
        ('WESTMEATH', 'Westmeath'),
        ('WEXFORD', 'Wexford'),
        ('WICKLOW', 'Wicklow'),
    )
    #   FIELDS
    title = models.CharField(
        max_length=255
    )
    description = models.CharField(
        max_length=14,
        choices=ENT_TYPES,
        default='BAND'
    )
    genre = models.CharField(
        max_length=9,
        choices=GENRE_TYPES,
        default='ROCK'
    )
    location = models.CharField(
        max_length=10,
        choices=COUNTIES,
        default='ANTRIM'
    )
    image = models.ImageField(
        upload_to='media/'
    )
    bio = models.TextField()

    #   display title in admin instead of "Entertainer object"
    def __unicode__(self):
        return self.title

    def desc_remove_underscore(self):
        return self.description.replace('_',' ')

    def init_cap_genre(self):
        return self.genre[0].upper()+self.genre[1:].lower()

    def init_cap_location(self):
        return self.location[0].upper()+self.location[1:].lower()
