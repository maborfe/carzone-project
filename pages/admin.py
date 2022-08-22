from django.contrib import admin

from .models import *


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'icone', 'name', 'position']
    list_display_links = ['id','icone','name', ]
    list_editable = ['position']

admin.site.register(Team, TeamAdmin)


