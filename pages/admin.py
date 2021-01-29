from django.contrib import admin
from contents.models import (
    Service,
    Project
    )



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order',]
    ordering = ['order']
    search_fields = ['title', 'details']



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'details']
    ordering = ['created']
    search_fields = ['title', 'details', 'project_url']
