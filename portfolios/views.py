from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from .models  import Project
from .forms import ContactForm


def index(request):

    return render(request, "portfolios/index.html")

def projects(request):
    project = Project.objects.all().order_by('-date')
    print(project)

    context = {
        'projects':project}

    return render(request, "portfolios/projects.html", context)

def resume(request):

    return render(request, "portfolios/resume.html")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'portfolios/contact.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'portfolios/contact.html', context)



