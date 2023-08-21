from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.template import loader
from contact.models import Testimonial


def index(request):
    """renders homepage"""
    testimonials = Testimonial.objects.filter(is_approved=True).order_by('-created_at')[:2] 
    context = {
        'testimonials': testimonials,
    }
    return render(request, 'home/index.html', context)