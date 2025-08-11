from django.contrib import admin
from .models import Music
# Register your models here.
admin.site.site_header = "Music Player Admin"
admin.site.site_title = "Music Player Admin Portal"
admin.site.index_title = "Welcome to the Music Player Admin Portal" 
admin.site.register(Music)