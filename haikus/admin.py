from django.contrib import admin
from .models import Haiku, Review

class ReviewInline(admin.TabularInline):
    model = Review


class HaikuAdmin(admin.ModelAdmin):
    inlines = [ReviewInline,]
    list_display = ("poem", "author",)

admin.site.register(Haiku, HaikuAdmin)