from django.contrib import admin

from blog.models import Blog, Comment, Likes


admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Likes)
