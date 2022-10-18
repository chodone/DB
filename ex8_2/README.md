# 8-2

## serializer.py
```py
from rest_framework import serializers
from .models import Music

class MusicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields= ('id', 'title')


class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'

```

## urls.py
```py
from django.urls import path
from . import views


urlpatterns = [

    path('musics/', views.music_list),
    path('musics/<int:music_pk>/', views.music_detail),

]
```

## views.py
```py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404

from .serializers import MusicListSerializer, MusicSerializer
from .models import Music


@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        musics = get_list_or_404(Music)
        serializer = MusicListSerializer(musics, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MusicSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)

    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)

        
    elif request.method == 'DELETE':
        music.delete()
        data = {
            'delete': f'음악{music_pk}번이 삭제되었습니다'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    
    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

```