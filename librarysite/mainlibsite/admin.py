from django.contrib import admin
from .models import *


class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'year_publish', 'short_info', 'image_book')
    list_display_links = ('name',)
    search_fields = ('name', 'short_info')
    prepopulated_fields = {"slug": ("name",)}


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name_author',)
    list_display_links = ('name_author',)
    search_fields = ('name_author',)
    prepopulated_fields = {"slug": ("name_author",)}


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'post', 'created', 'active',)
#     list_filter = ('active', 'created', 'updated',)
#     search_fields = ('name', 'email', 'body',)
#     prepopulated_fields = {"slug": ("name",)}


# admin.site.register(Comment, CommentAdmin)
admin.site.register(Books, LibraryAdmin)
admin.site.register(Author, AuthorAdmin)
