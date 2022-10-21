from turtle import title
from django.contrib import admin
from upload.models import Media



class Medias(admin.ModelAdmin):
    list_display = ['title', 'document']
    search_fields = ('title',)


admin.site.register(Media, Medias)
