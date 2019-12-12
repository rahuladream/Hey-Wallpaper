from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
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

    def wallpaper(self, obj):
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url = obj.image.url,
                width='100',
                height='90',
                )
        )

    def thumbnail(self, obj):
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url = obj.thumbnail.url,
                width='50',
                height='50',
                )
        )
    readonly_fields = ['wallpaper', 'thumbnail']
    list_display = ['category', 'total_views', 'total_download', 'is_active']
admin.site.register(Wallpaper, WallpaperAdmin)