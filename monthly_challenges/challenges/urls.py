from django.urls import path
from . import views  # imported views.py

urlpatterns = [
    path("", views.index, name="index"), # triggers /challenges/ PATH
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]  # List for URLs that is needed to be supported.
