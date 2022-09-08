from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def customIndex(request):
    return HttpResponse("Hello this is index123")

def detail(request, question_id):
    return HttpResponse("this is parameter question_id : %s" % question_id)

def results(request, question_id):
    return HttpResponse("result of question. question_id : %s" % question_id)

def vote(request, question_id):
    return HttpResponse("you are vote question %s." % question_id)