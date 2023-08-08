from django.shortcuts import render
# need for a response after the user request
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("This works!")

def february(request):
    return HttpResponse("This is february!")