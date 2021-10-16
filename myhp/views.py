from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader

my_lists =["今度行きたいみんなにもおすすめのラーメン屋", "1年記念日アルバム", "newalbum1","222"]


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def homemap(request):
    template = loader.get_template('homemap.html')
    context = {}
    return HttpResponse(template.render(context, request))

def makepost(request):
    template = loader.get_template('makepost.html')
    context = {}
    return HttpResponse(template.render(context, request))

def index2(request):
    template = loader.get_template('index2.html')
    context = {}
    return HttpResponse(template.render(context, request))

def indexwhenplacenametapped(request):
    template = loader.get_template('indexwhenplacenametapped.html')
    context = {"mylists": my_lists}
    return HttpResponse(template.render(context, request))