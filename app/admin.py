from django.contrib import admin
from .models import Category, Article, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_date', 'author')
    list_filter = ('category', 'published_date')
    search_fields = ('title', 'about', 'author')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'article', 'user_name', 'comment_date')
    list_filter = ('comment_date', 'article')
    search_fields = ('title', 'user_name', 'user_email', 'comment_text')
    date_hierarchy = 'comment_date'
    ordering = ('-comment_date',)
