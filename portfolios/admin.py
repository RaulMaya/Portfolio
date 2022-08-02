from django.contrib import admin
from .models import Project, Tag

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    # readonly_fields =  ("slug", )
    prepopulated_fields = {"slug":("title",)}
    list_filter = ("tag" ,"date")
    list_display = ("title", "date")


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
