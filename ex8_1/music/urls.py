from django.urls import path
from . import views


urlpatterns = [
    path("html/", views.music_html),
    path("json-1/", views.music_json_1),
    path("json-2/", views.music_json_2),
]
