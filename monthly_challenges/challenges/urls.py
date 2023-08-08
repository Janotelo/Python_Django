from django.urls import path
from . import views  # imported views.py

urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge)
]  # List for URLs that is needed to be supported.
