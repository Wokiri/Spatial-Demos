from django.contrib import admin
from contents.models import Service

# Register your models here.
@admin.register(Service)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'details')
