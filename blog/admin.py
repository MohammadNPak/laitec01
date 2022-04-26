import imp
from django.contrib import admin

# Register your models here.
from .models import Post, Comment, UserProfile


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
