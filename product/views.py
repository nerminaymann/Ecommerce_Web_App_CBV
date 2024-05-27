import json

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    context = {}
    return HttpResponse(json.dumps(context), content_type="application/json")
