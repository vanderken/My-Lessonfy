from django.contrib import admin

from .models import Collection, Lesson, Panel, Pin, User, UserSettings


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_staff", "is_active", "date_joined")
    search_fields = ("email",)
    ordering = ("email",)


@admin.register(UserSettings)
class UserSettingsAdmin(admin.ModelAdmin):
    list_display = ("user", "font_size", "line_spacing", "theme", "sound")


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "color")
    list_filter = ("user",)


class PanelInline(admin.TabularInline):
    model = Panel
    extra = 2


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at")
    list_filter = ("user",)
    inlines = [PanelInline]


@admin.register(Panel)
class PanelAdmin(admin.ModelAdmin):
    list_display = ("lesson", "order")
    list_filter = ("lesson",)


@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    list_display = ("text_snippet", "panel", "collection", "start_offset", "end_offset")
    list_filter = ("collection",)