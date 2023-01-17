from django.contrib import admin
from django.contrib.admin import ModelAdmin

from blog.models import Comment, Post


# Register your models here.


class PostAdmin(ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status", "created_on")
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}

    summernote_fields = ("content",)


def approve_comments(request, queryset):
    queryset.update(active=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]


admin.site.register(Post, PostAdmin)