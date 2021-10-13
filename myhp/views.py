from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def homemap(request):
    template = loader.get_template('homemap.html')
    context = {}
    return HttpResponse(template.render(context, request))

def post(request):
    template = loader.get_template('post.html')
    context = {}
    return HttpResponse(template.render(context, request))

def index2(request):
    template = loader.get_template('index2.html')
    context = {}
    return HttpResponse(template.render(context, request))