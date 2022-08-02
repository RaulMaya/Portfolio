from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from .models  import Project


def index(request):

    return render(request, "portfolios/index.html")

def projects(request):
    project = Project.objects.all()
    print(project)


    return render(request, "portfolios/projects.html", {
        'projects':project})

def resume(request):

    return render(request, "portfolios/resume.html")

def interests(request):

    return render(request, "portfolios/interests.html")



