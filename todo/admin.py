from django.contrib import admin

from .models import Todo, Tag, TodoComment


class TodoCommentInline(admin.StackedInline):
    extra = 1
    model = TodoComment


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    inlines = (TodoCommentInline,)
