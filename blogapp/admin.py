from django.contrib import admin

from .models import Topic, Comment, Image

class TopicAdmin(admin.ModelAdmin):
    list_display= ['id', 'title', 'date_created', 'date_modified']

class CommentAdmin(admin.ModelAdmin):
    list_display= ['id', 'topic', 'topic', 'text', 'date_created']

admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Image)

