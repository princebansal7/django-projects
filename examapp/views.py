from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def testpaper(req):
    res = "<h1>Hello, This is test paper view</h1>"
    return HttpResponse(res)


def mcq(req):
    res = "<h1>This is mcq view</h1>"
    return HttpResponse(res)
