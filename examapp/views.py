from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def testpaper(req):
    template = loader.get_template("testpaper.html")
    res = template.render()
    return HttpResponse(res)


def mcq(req):
    # assume we got below data from database
    question = "Best Character?"
    a = "Tom"
    b = "Tanjiro"
    c = "Mina"
    d = "Mikasa"
    options = [a, c, b, d]
    context = {"question": question, "options": options}

    template = loader.get_template("mcq.html")
    res = template.render(context, req)
    return HttpResponse(res)
