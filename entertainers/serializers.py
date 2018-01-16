from rest_framework import serializers
from entertainers.models import Entertainer
from rest_framework.pagination import PaginationSerializer

class EntertainerSerializer(serializers.ModelSerializer):
    """
    Used to serialize the Entertainer Querysets to JSON. The fields to be serialized are:
    -   id
    -   title
    -   description
    -   genre
    -   location
    """
    #customField = serializers.ReadOnlyField(source='test')

    my_field = serializers.SerializerMethodField('is_named_bar')

    def is_named_bar(self, foo):
        return foo.name == "bar"

    class Meta:
            model = Entertainer
            fields = ('id','title','description','genre','location','bio_summary','profile_image_url','my_field')


