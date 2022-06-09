from django.contrib import admin
from django.utils.safestring import mark_safe

from posts.models import Post, Comment, Follow


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Управление постами."""

    list_display = ("pk", "text", "pub_date", "author", "get_html_image")
    list_display_links = ("pk", "text")
    date_hierarchy = "pub_date"
    search_fields = ("text",)
    empty_value_display = "-пусто-"

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" height=30>')

    get_html_image.short_description = "Картинка"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Управление комментариями."""

    list_display = ("pk", "text", "post", "author")
    list_display_links = ("pk", "text")
    date_hierarchy = "created"
    search_fields = ("text",)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Настройка административной панели для управления подписками."""

    list_display = ("pk", "user", "following")
    search_fields = (
        "user__username__startswith",
        "following__username__startswith",
    )
