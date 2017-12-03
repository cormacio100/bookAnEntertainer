from django import forms
from entertainers.models import Entertainer

class EntertainerRegistrationForm(forms.ModelForm):

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
