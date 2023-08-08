from django.urls import path
from . import views  # imported views.py

urlpatterns = [
    path("january", views.index)  # called the function in the views.
]  # List for URLS that is needed to be supported.