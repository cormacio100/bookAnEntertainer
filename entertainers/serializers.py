from rest_framework import serializers
from entertainers.models import Entertainer

class EntertainerSerializer(serializers.ModelSerializer):
    """
    Used to serialize the Entertainer model to JSON. The fields to be serialized are:
    -   id
    -   title
    -   description
    -   genre
    -   location
    """
    class Meta:
        model = Entertainer
        fields = ('id','title','description','genre','location')
