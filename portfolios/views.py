from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string


def index(request):

    return render(request, "portfolios/index.html")

def projects(request):

    return render(request, "portfolios/projects.html")

def resume(request):

    return render(request, "portfolios/resume.html")

def interests(request):

    return render(request, "portfolios/interests.html")

