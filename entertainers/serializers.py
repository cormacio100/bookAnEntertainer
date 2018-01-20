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

    """
    def __init__(self, *args, **kwargs):
        #self.paginator = kwargs.get('paginator')
        self.num_pages = kwargs.get('num_pages')
        #self.count = kwargs.get('count')
        super(EntertainerSerializer, self).__init__(*args, **kwargs)
    """

    def __init__(self, entertainers, many=False,num_pages=0, count=0):
        self.num_pages = num_pages
        self.count = count
        super(EntertainerSerializer, self).__init__(entertainers, many=False)

    page_count = serializers.SerializerMethodField('num_pages_func')
    record_count = serializers.SerializerMethodField('count_func')

    def num_pages_func(self,foo):
        return self.num_pages

    def count_func(self,foo):
        return self.count

    class Meta:
            model = Entertainer
            fields = ('id','title','description','genre','location','bio_summary','profile_image_url','page_count','record_count')


