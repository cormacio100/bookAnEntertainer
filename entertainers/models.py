# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
class Entertainer(models.Model):

    #   DEFINE CHOICES LISTS WITH CONSTANTS
    ENT_TYPES = (
        ('Band', 'Band'),
        ('Solo', 'Solo')
    )
    GENRE_TYPES = (
        ('Rock', 'Rock'),
        ('Metal', 'Metal'),
        ('Punk', 'Punk'),
        ('Blues', 'Blues'),
        ('Jazz', 'Jazz'),
        ('Classical', 'Classical'),
        ('Reggae', 'Reggae'),
        ('Ska', 'Ska'),
        ('Dance', 'Dance'),
        ('Funk', 'Funk'),
    )
    COUNTIES = (
        ('Antrim', 'Antrim'),
        ('Armagh', 'Armagh'),
        ('Carlow', 'Carlow'),
        ('Cavan', 'Cavan'),
        ('Clare', 'Clare'),
        ('Cork', 'Cork'),
        ('Derry', 'Derry'),
        ('Donegal', 'Donegal'),
        ('Down', 'Down'),
        ('Dublin', 'Dublin'),
        ('Fermanagh', 'Fermanagh'),
        ('Galway', 'Galway'),
        ('Kerry', 'Kerry'),
        ('Kildare', 'Kildare'),
        ('Kilkenny', 'Kilkenny'),
        ('Laois', 'Laois'),
        ('Leitrim', 'Leitrim'),
        ('Limerick', 'Limerick'),
        ('Longford', 'Longford'),
        ('Louth', 'Louth'),
        ('Mayo', 'Mayo'),
        ('Meath', 'Meath'),
        ('Monaghan', 'Monaghan'),
        ('Offaly', 'Offaly'),
        ('Roscommon', 'Roscommon'),
        ('Sligo', 'Sligo'),
        ('Tipperary', 'Tipperary'),
        ('Tyrone', 'Tyrone'),
        ('Waterford', 'Waterford'),
        ('Westmeath', 'Westmeath'),
        ('Wexford', 'Wexford'),
        ('Wicklow', 'Wicklow'),
    )
    LANGUAGE_TYPES = (
        ('English', 'English'),
        ('Irish', 'Irish'),
        ('French', 'French'),
        ('Spanish', 'Spanish'),
        ('German', 'German'),
    )
    MUSIC_CLASSIFICATION = (
        ('Original','Original'),
        ('Covers', 'Covers'),
        ('Comedy', 'Comedy'),
        ('Parody', 'Parody'),
    )
    GIG_LENGTH_OPTIONS = (
        ('60','60'),
        ('90', '90'),
        ('120', '120'),
        ('180', '180'),
        ('240', '240'),
    )
    SET_UP_REQUIREMENTS = (
        ('Power Source','Power Source'),
        ('Stage Cover - If Outside', 'Stage Cover - If Outside'),
        ('Accomodation', 'Accomodation'),
        ('Food', 'Food'),
        ('Beverages', 'Beverages')
    )
    #   FIELDS
    title = models.CharField(
        max_length = 255
    )
    description = models.CharField(
        max_length = 14,
        choices = ENT_TYPES,
        default = 'Band'
    )
    genre = models.CharField(
        max_length = 9,
        choices = GENRE_TYPES,
        default = 'Rock'
    )
    location = models.CharField(
        max_length = 10,
        choices = COUNTIES,
        default = 'Antrim'
    )
    image = models.ImageField(
        upload_to = 'media/'
    )
    language = MultiSelectField(
        choices = LANGUAGE_TYPES,
        default = 'English'
    )
    music = MultiSelectField(
        choices = MUSIC_CLASSIFICATION,
        default = 'Originals'
    )
    gig_length_from = models.CharField(
        max_length = 3,
        choices = GIG_LENGTH_OPTIONS,
        default = 60
    )
    gig_length_to = models.CharField(
        max_length = 3,
        choices = GIG_LENGTH_OPTIONS,
        default = 90
    )
    bio = models.TextField()
    set_list = models.TextField(default='All genres and decades.')
    influences = models.TextField(default='All Genres and decades.')

    #   returns a CHARFIELD OF COMMA SEPARATED VALUES
    set_up_requirements = MultiSelectField(
        choices = SET_UP_REQUIREMENTS,
        default = 'Power Source'
    )

    #   SPECIAL FUNCTIONS
    #   display title in admin instead of "Entertainer object"
    def __unicode__(self):
        return self.title

    def desc_remove_underscore(self):
        return self.description.replace('_',' ')

    def init_cap_genre(self):
        return self.genre[0].upper()+self.genre[1:].lower()

    def init_cap_location(self):
        return self.location[0].upper()+self.location[1:].lower()

    def bio_summary(self):
        return self.bio[:100]

    def language_list_as_str(self):
        i=0
        language_str = ''
        while i<len(self.language):
            language_str += self.language[i]+','
            i+=1
        return language_str.rstrip(',')

    def music_type_as_str(self):
        i = 0
        music_type_str = ''
        while(i<len(self.music)):
            music_type_str += self.music[i] + ','
            i += 1
        return music_type_str.rstrip(',')

    def gig_length_as_str(self):
        return self.gig_length_from + ' - ' + self.gig_length_to + ' minutes'

    def set_up_requirements_str_split(self):
        return  self.set_up_requirements.split(',')


