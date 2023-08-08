from django.shortcuts import render
# need for a response after the user request
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "This is april.",
    "may": "This is may.",
    "june": "This is june.",
    "july": "This is july.",
    "august": "This is august.",
    "september": "This is september.",
    "october": "This is october.",
    "november": "This is november.",
    "december": "This is december."
}


def monthly_challenge_by_number(request, month):
    # .keys is a part of a dictionary | key:value pair
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)

    except:
        return HttpResponseNotFound('This month is not supported!')
