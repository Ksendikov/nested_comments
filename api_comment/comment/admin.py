from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Comment, Post

admin.site.register(Post)

admin.site.register(Comment, MPTTModelAdmin)