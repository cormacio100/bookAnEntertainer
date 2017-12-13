from django import forms
from entertainers.models import Entertainer

class EntertainerRegistrationForm(forms.ModelForm):

    #   constructor
    def __init__(self,user,*args,**kwargs):
        self.user = user
        super(EntertainerRegistrationForm,self).__init__(*args,**kwargs)

    def save(self,commit=True):
        #   save(commit=False) prevents the form from auto saving
        #   The instance of the form is what gets saved
        instance = super(EntertainerRegistrationForm,self).save(commit=False)

        #   auto set the user instance to that provided by the view
        instance.user = self.user

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
                    'image2',
                    'image3',
                    'image4',
                    'image5',
                    'language',
                    'music',
                    'gig_length_from',
                    'gig_length_to',
                    'bio',
                    'set_list',
                    'influences',
                    'set_up_requirements',
                    'travel_distance',
                    'min_price',
                    'max_price',
                    'soundcloud_audio',
                    'youtube_video')


