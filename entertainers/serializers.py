from rest_framework import serializers
from entertainers.models import Entertainer
#from rest_framework.pagination import PaginationSerializer


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

    def __init__(self, *args, **kwargs):
        self.paginator = kwargs.get('paginator')
        super(EntertainerSerializer, self).__init__(*args, **kwargs)

    paginate = serializers.SerializerMethodField('pages')

    def pages(self, foo):
        return self.paginator

    class Meta:
            model = Entertainer
            fields = ('id','title','description','genre','location','bio_summary','profile_image_url','paginate')


