from django.shortcuts import render
# need for a response after the user request
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "Eat no meat for the entire month!"
    elif month == 'february':
        challenge_text = "Walk for at least 20 minutes every day!"
    elif month == 'march':
        challenge_text = "Learn Django for at least 20 minutes every day!"
    elif month == 'april':
        challenge_text = ""
    elif month == 'may':
        challenge_text = ""
    elif month == 'june':
        challenge_text = ""
    elif month == 'july':
        challenge_text = ""
    elif month == 'august':
        challenge_text = ""
    elif month == 'september':
        challenge_text = ""
    elif month == 'october':
        challenge_text = ""
    elif month == 'november':
        challenge_text = ""
    elif month == 'december':
        challenge_text = ""
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
