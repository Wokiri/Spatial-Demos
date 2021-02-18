from django.contrib import admin

from .models import UserPoint

@admin.register(UserPoint)
class UserPointAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')