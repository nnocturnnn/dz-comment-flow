from django.urls import path

from . import views

urlpatterns = [
    path("", views.base_view, name="spa"),
    path("comment_add", views.comment_add, name="comment_add"),
    path("like_add", views.like_add, name="like_add"),
    path("like_remove", views.like_remove, name="like_remove"),
]
