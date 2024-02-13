from django.contrib import admin
from django.contrib.auth.models import User
from .models import Classroom, Asset, Chatroom


admin.site.site_header = 'MC² administration'


class AssetInline(admin.StackedInline):
    model = Asset


class ChatroomInline(admin.TabularInline):
    model = Chatroom


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    inlines = [
        AssetInline,
        ChatroomInline,
    ]
