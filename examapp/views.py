from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def testpaper(req):
    template = loader.get_template("testpaper.html")
    res = template.render()
    return HttpResponse(res)


def mcq(req):
    res = "<h1>This is mcq view</h1>"
    return HttpResponse(res)
