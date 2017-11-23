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
        ('Electronic', 'Electronic'),
        ('Funk', 'Funk'),
        ('Trad', 'Trad'),
        ('Country', 'Country'),
        ('Soul', 'Soul'),
        ('Other', 'Other'),
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
    PRICE_PER_HOUR = (
        ('100','100'),
        ('200','200'),
        ('300','300'),
        ('400','400'),
        ('500','500'),
        ('600','600'),
        ('700','700'),
        ('800','800'),
        ('900','900'),
        ('1000','1000'),
        ('1100','1100'),
        ('1200','1200'),
        ('1300','1300'),
        ('1400','1400'),
        ('1500','1500'),
        ('1600','1600'),
        ('1700','1700'),
        ('1800','1800'),
        ('1900','1900'),
        ('2000','2000'),
        ('2100','2100'),
        ('2200','2200'),
        ('2300','2300'),
        ('2400','2400'),
        ('2500','2500'),
    )
    SET_UP_REQUIREMENTS = (
        ('Power Source','Power Source'),
        ('Stage Cover - If Outside', 'Stage Cover - If Outside'),
        ('Accomodation', 'Accomodation'),
        ('Food', 'Food'),
        ('Beverages', 'Beverages')
    )
    TRAVEL_OPTIONS = {
        ('nationwide','nationwide'),
        ('same province','same province'),
        ('same county','same county')
    }
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
    profile_image = models.ImageField(
        upload_to = 'media/profile/',
        default = 'media/no_image.png'
    )

    image1 = models.ImageField(
        upload_to = 'media/img1/',
        default = 'media/no_image.png'
    )
    image2 = models.ImageField(
        upload_to = 'media/img2/',
        default='media/no_image.png'
    )
    image3 = models.ImageField(
        upload_to = 'media/img3/',
        default='media/no_image.png'
    )
    image4 = models.ImageField(
        upload_to = 'media/img4/',
        default='media/no_image.png'
    )
    image5 = models.ImageField(
        upload_to = 'media/img5/',
        default='media/no_image.png'
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
    set_list = models.TextField(default = 'All genres and decades.')
    influences = models.TextField(default = 'All Genres and decades.')
    #   returns a CHARFIELD OF COMMA SEPARATED VALUES
    set_up_requirements = MultiSelectField(
        choices = SET_UP_REQUIREMENTS,
        default = 'Power Source'
    )
    travel_distance = models.CharField(
        max_length = 13,
        choices = TRAVEL_OPTIONS,
        default = 'nationwide'
    )
    min_price = models.CharField(
        max_length = 4,
        choices = PRICE_PER_HOUR,
        default = '100'
    )
    max_price = models.CharField(
        max_length = 4,
        choices = PRICE_PER_HOUR,
        default = '500'
    )
    soundcloud_audio = models.TextField(default = 'https://soundcloud.com/')
    youtube_video = models.TextField(default = 'https://www.youtube.com')


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

    def price_per_hour_str(self):
        return '€' + self.min_price + ' - €' + self.max_price

    #   need to fit soundcloud link in the carousel
    def soundcloud_audio_re_class(self):
        #   2 sized of iframe available with soundcloud
        substr1 = 'width="100%" height="300"'
        substr2 = 'width="100%" height="166"'
        #   new class for the iframe so that it fits in the carousel
        re_class = 'class="d-block w-100 img-centered carouselled"'

        if self.soundcloud_audio.find(substr1):
            return self.soundcloud_audio.replace(substr1,re_class)

        if self.soundcloud_audio.find(substr2):
            return self.soundcloud_audio.replace(substr2,re_class)

    #   need to fit the youtube link in the carousel
    def youtube_video_re_class(self):
        substr1 = 'width="560" height="315"'
        re_class = 'class="d-block w-100 img-centered carouselled"'

        if self.youtube_video.find(substr1):
            return self.youtube_video.replace(substr1,re_class)

