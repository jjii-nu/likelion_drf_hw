from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Singer, Song, Tag
from .serializer import SingerSerializer, SongSerializer, TagSerializer

from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET','POST'])
def singer_list_create(request):

    if request.method == 'GET':
        singers = Singer.objects.all()
        serializer = SingerSerializer(singers, many=True)
        return Response(data=serializer.data)
    
    if request.method == 'POST':
        serializer = SingerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            content = request.data['content']
            singer = get_object_or_404(Singer, id = serializer.data['id'])
            tags = [words[1:] for words in content.split(' ') if words.startswith('#')]
            for t in tags:
                try:
                    tag = get_object_or_404(Tag, name=t)
                except:
                    tag = Tag(name = t)
                    tag.save()
                singer.tag.add(tag)
            singer.save()
            return Response(data=SingerSerializer(singer).data)

@api_view(['GET','PATCH','DELETE'])
def singer_detail_update_delete(request, singer_id):
    singer = get_object_or_404(Singer, id=singer_id)

    if request.method == 'GET':
        serializer = SingerSerializer(singer)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = SingerSerializer(instance=singer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            singer = get_object_or_404(Singer, id = serializer.data['id'])
            singer.tag.clear()
            content = request.data['content']
            tags = [words[1:] for words in content.split(' ') if words.startswith('#')]
            for t in tags:
                try:
                    tag = get_object_or_404(Tag, name=t)
                except:
                    tag = Tag(name = t)
                    tag.save()
                singer.tag.add(tag)
            singer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        singer.delete()
        data = {
            'deleted_singer': singer_id
        }
        return Response(data)
    
@api_view(['GET', 'POST'])
def song_read_create(request, singer_id):
    singer = get_object_or_404(Singer, id=singer_id)

    if request.method == 'GET':
        songs = Song.objects.filter(singer=singer)
        serializer = SongSerializer(songs, many=True)
        return Response(data=serializer.data)
    
    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(singer=singer)
            return Response(serializer.data)
        
@api_view(['GET'])
def find_tag(request, tag_name):
    tag = get_object_or_404(Tag, name = tag_name)
    if request.method == 'GET':
        singer = Singer.objects.filter(tag__in = [tag])
        serializer = SingerSerializer(singer, many=True)
        return Response(data = serializer.data)