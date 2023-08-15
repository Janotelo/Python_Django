from django.urls import path

from . import views

urlspattern = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    # /posts/my-first-post {slug format}
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")
]