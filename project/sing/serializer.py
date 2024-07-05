from rest_framework import serializers
from .models import *

#다중이미지구현코드추가
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id','image']
#여기까지
class SingerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    songs = serializers.SerializerMethodField(read_only=True)

    def get_songs(self, instance):
        serializer = SongSerializer(instance.songs, many=True)
        return serializer.data
    
    tag = serializers.SerializerMethodField()
    def get_tag(self, instance):
        tags = instance.tag.all()
        return [tag.name for tag in tags]
    class Meta:
        model = Singer
        fields = ['id','name','content','tag','debut','songs','images']

    images = ImageSerializer(many=True, read_only=True)

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ['singer']

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'