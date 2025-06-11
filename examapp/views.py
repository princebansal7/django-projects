from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def testpaper(req):
    template = loader.get_template("testpaper.html")
    res = template.render()
    return HttpResponse(res)


def mcq(req):
    template = loader.get_template("mcq.html")
    res = template.render()
    return HttpResponse(res)
