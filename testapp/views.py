from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def greeting(req):
    res = "<h1>Hello, This is first django view</h1>"
    return HttpResponse(res)


def about(req):
    res = "<h1>This is About view</h1>"
    return HttpResponse(res)


def contact(req):
    res = "<h1>This is Contact view</h1>"
    return HttpResponse(res)
