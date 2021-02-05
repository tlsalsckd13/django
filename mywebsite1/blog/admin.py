from django.contrib import admin
from blog.models import Category, Music, Artist, Album, PlayList

# Register your models here.
admin.site.register(Category)
admin.site.register(Music)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(PlayList)