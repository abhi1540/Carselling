from django.contrib import admin
from .models import Team, TeamAdmin

# Register your models here.
admin.site.register(Team,TeamAdmin)