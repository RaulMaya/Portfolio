from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("projects", views.projects, name="projects"),
    path("resume", views.resume, name="resume"),
    path("interests", views.interests, name="interests"),
    path("<str:project>", views.project, name="project-page"),
]