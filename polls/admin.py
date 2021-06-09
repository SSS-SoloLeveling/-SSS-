from django.contrib import admin

from .models import Task


class SSS(admin.ModelAdmin):
    search_fields=('title', 'task',)
    list_display = ('title','task',)
admin.site.register(Task, SSS)
