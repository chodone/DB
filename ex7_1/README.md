# articles

## serializers.py
```py
from rest_framework import serializers
from .models import Article



class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
```

## urls.py

```py
from django.urls import path
from . import views


urlpatterns = [
    path('html/', views.article_html),
    path('json-1/', views.article_json_1),
    path('json-2/', views.article_json_2),
    path('json-3/', views.article_json_3),
]

```



## views.py
```py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .serializers import ArticleListSerializer
from .models import Article



# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
            }
        )
    return JsonResponse(articles_json, safe=False)


def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles, fields=('title', 'content',))
    return HttpResponse(data, content_type='application/json')

@api_view(['GET'])
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

```