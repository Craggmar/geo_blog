from django.contrib import admin

from .models import BlogUser

admin.site.register(BlogUser)
class CommentAdmin(admin.ModelAdmin):
    list_display= ['id', 'user']