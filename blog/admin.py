from django.contrib import admin

import blog.admin

from .models import Blog, Category, Tag, Comments

# Register your models here.

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comments)


# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at', 'author')
#     list_filter = ('author',)
#     search_fields = ('title',)
#     ordering = ('title',)
#     date_hierarchy = 'created_at'

# admin.site.register(blog, BlogAdmin)
