from django.contrib import admin
from .models import Post


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "author", "created_at", "updated_at")


admin.site.register(Post, BlogAdmin)
