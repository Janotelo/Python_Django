from django.urls import path
from . import views  # imported views.py

urlpatterns = [
    path("<month>", views.monthly_challenge)
]  # List for URLs that is needed to be supported.
