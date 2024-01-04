from django.contrib import admin

from .models import Attachment, Comment, Like


class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 1  # Number of extra forms to display


class CommentAdmin(admin.ModelAdmin):
    inlines = [
        AttachmentInline,
    ]


admin.site.register(Comment, CommentAdmin)
admin.site.register(Attachment)
admin.site.register(Like)
