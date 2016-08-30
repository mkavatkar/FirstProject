from django.shortcuts import render
from django.http import HttpResponse


# index/ view for the polls app
def index(request):
    return HttpResponse("Hello World, Location: index/")


# Get the details of questions and display in this view
def detail(request, question_id):
    return HttpResponse("You are looking at Question %s" % question_id)


# Result view
def results(request, question_id):
    response = "You are looking at the result of %s"
    return HttpResponse(response % question_id)


# Voting view
def vote(request, question_id):
    return HttpResponse("You are voting on Question %s" % question_id)
