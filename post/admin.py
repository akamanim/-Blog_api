from django.contrib import admin
from .models import Category, Tag, Post


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)


# fuser -k 8000/tcp
# 8001