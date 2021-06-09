from django.contrib import admin

from .models import Task


class SSS(admin.ModelAdmin):
    search_fields=('title',)
admin.site.register(Task, SSS)