from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from blog.models import Post, Tag, Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'created_time', 'modified_time']


admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Tag)
admin.site.register(Category)