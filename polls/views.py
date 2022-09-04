from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def customIndex(request):
    return HttpResponse("Hello this is index123")

