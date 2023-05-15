from django.contrib import admin
from .models import Category, Tag, Post, Like, Rating


admin.site.register(Category)
admin.site.register(Tag)
# admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Rating)



class RatingInline(admin.TabularInline):
    model = Rating

class LikeInline(admin.TabularInline):
    model = Like

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'category', 'Рэйтинг','все_лайки')
    inlines = [RatingInline, LikeInline]
    search_fields = ['title', 'body']
    search_help_text = 'BumBye'
    ordering = ['created_at']
    list_filter = ['category__title']

    def Рэйтинг(self, obj):
        from django.db.models import Avg
        result = obj.ratings.aggregate(Avg('rating'))
        return result['rating__avg']
    def все_лайки(self, obj):
        result = obj.likes.count()
        return result

admin.site.register(Post, PostAdmin)
# fuser -k 8000/tcp
# 8001