from django.contrib.gis import admin
from .models import (
    RetailStore,
    SampledIssue,
    )

admin.site.register(RetailStore, admin.OSMGeoAdmin)


@admin.register(SampledIssue)
class SampledIssueAdmin(admin.ModelAdmin):
    list_filter = ['counties']
    search_fields = ['issue']
    ordering = ['issue']