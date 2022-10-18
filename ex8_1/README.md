# 8-1

## models.py

```py
from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```


## serializers.py

```py
import imp
from rest_framework import serializers
from .models import Music


class MusicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields= '__all__'

```


## urls.py

```py
from django.urls import path
from . import views


urlpatterns = [
    path("html/", views.music_html),
    path("json-1/", views.music_json_1),
    path("json-2/", views.music_json_2),
]
```


## views.py

```py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import Music
from .serializers import MusicListSerializer


# Create your views here.
def music_html(request):
    musics = Music.objects.all()
    context = {
        "musics": musics,
    }
    return render(request, "music/music.html", context)


def music_json_1(request):
    musics = Music.objects.all()
    musics_json = []

    for music in musics:
        musics_json.append(
            {
                "id": music.pk,
                "title": music.title,
                "content": music.content,
            }
        )
    return JsonResponse(musics_json, safe=False)


def music_json_2(request):
    musics = Music.objects.all()
    data = serializers.serialize(
        "json",
        musics,
        fields=(
            "title",
            "content",
        ),
    )
    return HttpResponse(data, content_type="application/json")

@api_view(['GET'])
def music_json_3(request):
    musics = Music.objects.all(request)
    serializer = MusicListSerializer(musics, many=True)
    return Response(serializer.data)
```
