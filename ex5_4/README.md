# 1 오류창

## movies - models.py

```py
like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'like_movies' )
```


# 2 좋아요 버튼 수정

## movies - views.py

```py
@require_POST
def likes(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)

        if movie.like_users.filter(pk=request.user.pk).exists():
            # if request.user in movie.like_users.all():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
        return redirect("movies:index")
    return redirect("accounts:login")
```


# 3 팔로우 버튼 수정

## accounts - profile.html
```html
{% extends 'base.html' %}

{% block content %}
<h1>{{ person.username }}님의 프로필</h1>
<br>
<div> 
  <p>
    팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
  </p>

  {% if request.user != person %}
  
    <div>
      <form action="{% url 'accounts:follow' person.pk %}" method="POST">
        {% csrf_token %}
        {% if user in person.followers.all %}
          <button class="btn btn-outline-primary btn-sm">팔로우 취소</button>
        {% else %}
          <button class="btn btn-primary btn-sm">팔로우</button>
        {% endif %}
      </form>
    </div>
  
  {% endif %}
</div>

<hr>

<h2>{{ person.username }}'s 게시글</h2>
<br>
{% for movie in person.movie_set.all %}
	<!-- person.article_set & person.comment_set -->
	<div>{{ movie.title }}</div>
{% endfor %}

<hr>

<h2>{{ person.username }}'s 댓글</h2>
<br>
{% for comment in person.comment_set.all %}
  <div>{{ comment.content }}</div>
{% endfor %}

<hr>

<a href="{% url 'movies:index' %}" class="btn btn-secondary btn-sm">이전</a>
{% endblock  %}
```
