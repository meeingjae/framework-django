from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Question

def customIndex(request):
    latestQuestionList = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latestQuestionList])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("this is parameter question_id : %s" % question_id)

def results(request, question_id):
    return HttpResponse("result of question. question_id : %s" % question_id)

def vote(request, question_id):
    return HttpResponse("you are vote question %s." % question_id)