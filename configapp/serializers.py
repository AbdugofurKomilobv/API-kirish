from rest_framework import  serializers

from .models import *


    
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    actors =  ActorSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = "__all__"