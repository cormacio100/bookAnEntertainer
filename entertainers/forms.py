from django import forms
from entertainers.models import Entertainer


class EntertainerRegistrationForm(forms.ModelForm):


    #   constructor
    def __init__(self,user,*args,**kwargs):

           # TO DO
           # RETRIEVE THE URLS LIST FROM KWARGS
           #     _urls = kwargs.pop('_urls',None)

            #   RETRIEVE THE SEPARATE URLS OF THE IMAGES
            #if _urls is not None:
            #    self.profile_image = _urls[0]
            #    self.img1 = _urls[1]

        #_urls = kwargs.pop('_urls', None)
        #if _urls is not None:
         #   self.profile_image = _urls[0]
          #  self.image1 = _urls[1]

        self.user = user
        super(EntertainerRegistrationForm,self).__init__(*args,**kwargs)

    def save(self,commit=True):
        #   save(commit=False) prevents the form from auto saving
        #   The instance of the form is what gets saved
        instance = super(EntertainerRegistrationForm,self).save(commit=False)

        #   auto set the user instance to that provided by the view
        instance.user = self.user

        #   auto set the image instance to that provided by the view
       # instance.profile_image = self.profile_image
        #instance.image1 = self.image1


        #    TO DO
        #    AUTO SET THE USER INSTANCE TO THAT PROVIDED BY THE VIEW
        #        instance.profile_image = self.profile_image
        #        instance.img1 = self.img1

        if commit:
            instance.save()
        return instance

    #   Tell Django which model to used to create the form
    class Meta:
        model = Entertainer
        fields = ('title',
                    'description',
                    'genre',
                    'location',
                    'profile_image',
                    'image1',
                    #'image2',
                    #'image3',
                    #'image4',
                    #'image5',
                    'language',
                    'music',
                    'gig_length_from',
                    'gig_length_to',
                    'bio',
                    'set_list',
                    'influences',
                    'travel_distance',
                    'min_price',
                    'max_price',
                    'soundcloud_audio',
                    'youtube_video',
                  'set_up_requirements',)


