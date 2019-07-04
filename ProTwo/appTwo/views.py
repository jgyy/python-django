"""Application 2 views"""
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    """
    :param request: http request
    :return: My Second Project
    """
    return HttpResponse("<em>My Second Project</em>")
