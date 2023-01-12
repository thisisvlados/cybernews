from django.contrib import admin
from .models import News, Category, Comments


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'created', 'moderation')


admin.site.register(Comments, CommentAdmin)
admin.site.register(News)
admin.site.register(Category)