from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.template import loader


def index(request):
    """renders homepage"""
    template = loader.get_template('home/index.html')
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return HttpResponse(template.render(context, request))