from django.contrib import admin
from apps.news.models import Category, Post, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name","slug","is_active","created_at",
    )
    list_display_links = ("id", "name")
    list_filter = ("is_active","created_at",)
    search_fields = ("name","slug",)
    prepopulated_fields = {"slug": ("name",),}
    ordering = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "created_at",)
    list_display_links = ("id", "name")
    search_fields = ("name","slug")
    prepopulated_fields = {"slug": ("name",),}
    ordering = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id", "title", "author", "category",
        "status", "is_active",  "views_count",
        "updated_at", "created_at",
    )
    list_display_links = ("id", "title")
    list_filter = (
        "status", "is_active",
        "category",  "tags",
        "created_at", "updated_at",
    )
    search_fields = (
        "title", "short_description", "content", 
        "author__username", "category__name",
    )
    prepopulated_fields = {"slug": ("title",),}
    filter_horizontal = ("tags",)
    readonly_fields = (
        "views_count", "created_at", "updated_at",
    )
    autocomplete_fields = ("author", "category",)
    ordering = ("-created_at",)