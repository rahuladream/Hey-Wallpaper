from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    prepopulated_fields ={'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    prepopulated_fields ={'slug': ('name',)}
admin.site.register(Tag, TagAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'rate', 'post_id']
admin.site.register(Rating, RatingAdmin)


class WallpaperAdmin(admin.ModelAdmin):
    list_display = ['category', 'total_views', 'total_download']
admin.site.register(Wallpaper, WallpaperAdmin)