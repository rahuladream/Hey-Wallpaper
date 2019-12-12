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
