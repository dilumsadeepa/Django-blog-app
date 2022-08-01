from django.contrib import admin

from .models import Post, Blog

admin.site.register(Blog)
admin.site.register(Post)
