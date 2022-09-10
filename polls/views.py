from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
from .models import Question


def customIndexV1(request):
    latestQuestionList = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latestQuestionList])
    return HttpResponse(output)


def customIndexV2(request):
    latestQuestionList = Question.objects.order_by('-pub_date')[:5]

    template = loader.get_template('polls/index.html')
    context = {
        'latestQuestionList': latestQuestionList
    }
    # output = ', '.join([q.question_text for q in latestQuestionList])
    return HttpResponse(template.render(context, request))


def customIndexV3(request):
    latestQuestionList = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latestQuestionList': latestQuestionList
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("this is parameter question_id : %s" % question_id)


def detailRaiseNotFound(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse("result of question. question_id : %s" % question_id)


def vote(request, question_id):
    return HttpResponse("you are vote question %s." % question_id)
