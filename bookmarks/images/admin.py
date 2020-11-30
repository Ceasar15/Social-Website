from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Image
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']



admin.site.register(Image,ImageAdmin)
