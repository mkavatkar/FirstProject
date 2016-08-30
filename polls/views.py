from django.shortcuts import render
from django.http import HttpResponse


# index/ view for the polls app
def index(request):
    return HttpResponse("Hello World, Location: index/")
