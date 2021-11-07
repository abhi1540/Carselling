from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.

class Team(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

# This class required to formatting Team class
class TeamAdmin(admin.ModelAdmin):
    ''' For stylingthe photos in admin section you need to import format_html from django utils'''
    def thumbnail(self, object):
        return format_html('<img src="{}" width=40 style="border-radius: 50px">'.format(object.photo.url))

    thumbnail.short_description = 'photo'
    list_display = ('id', 'first_name', 'last_name', 'thumbnail', 'designation', 'created_date')
    list_display_links = ('id', 'first_name', 'thumbnail')
    search_fields = ('first_name', 'last_name')
    list_filter = ('designation',)
