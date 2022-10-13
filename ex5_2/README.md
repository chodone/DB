# accounts

## models.py
```py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

```

## urls.py
```py
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),

]

```

## views.py
```py
def profile(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username )
    context = {
        'person' : person,
    }
    return render(request, 'accounts/profile.html', context)

def follow(request, user_pk):
    User = get_user_model()
    me = request.user
    you = get_object_or_404(User, pk=user_pk)
    if me != you:
        if you.followers.filter(pk=me.pk).exists():
            #언팔로우
            you.followers.remove(me)
        else:
            #팔로우
            you.followers.add(me)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')

```

## index.html
```html
{% extends 'base.html' %}


{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <div>
    팔로워 : {{ person.followers.all|length }} / 팔로잉 : {{ person.followings.all|length }}
  </div>


  {% if request.user != person %}
  <div>
    <form action="{% url 'accounts:follow' person.pk %}" method="POST">
      {% csrf_token %}
      {% if request.user in person.followers.all %}
        <input type="submit" value="언팔로우">
      {% else %}
        <input type="submit" value="팔로우">
      {% endif %}
    </form>
  <div>
  {% endif %}

  <h2>{{ person.username }}이 작성한 모든 게시글</h2>
  {% for movie in person.movie_set.all %}
    <div>{{ movie.title }}</div>
  {% endfor %}

  <hr>

  <h2>{{ person.username }}이 작성한 모든 댓글</h2>
  {% for comment in person.comment_set.all %}
    <div>{{ comment.content }}</div>
  {% endfor %}

  <hr>


  <a href="{% url 'movies:index' %}">back</a>

{% endblock content %}
```
