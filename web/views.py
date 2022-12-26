from django.shortcuts import render
from django.http import HttpRequest
from django.template.response import TemplateResponse

# Create your views here.

def index(request: HttpRequest):
    template = 'index.html'
    context = {}
    return TemplateResponse(request, template, context=context)

def about(request: HttpRequest):
    template = 'about.html'
    context = {}
    return TemplateResponse(request, template, context=context)

