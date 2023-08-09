from django.shortcuts import render
# need for a response after the user request
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\"> {capitalized_month}  </a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    # .keys is a part of a dictionary | key:value pair
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    # reverse will refer to the name of the PATH in the URLs
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # added 3rd argument which is a dictionary
        return render(request, "challenges/challenge.html", {
            # used this key'value pair inside the HTML file
            "text": challenge_text,
            "month_name": month
        })

    except:
        # added HTML codes
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
