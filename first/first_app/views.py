"""Views"""
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    """
    :param request: http request
    :return: hello world text
    """
    return HttpResponse("Hello World!")
