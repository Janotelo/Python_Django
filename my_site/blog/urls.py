from django.urls import path

urlspattern = [
    path(""),
    path("posts"),
    path("posts/<slug:slug>") #/posts/my-first-post {slug format}
]