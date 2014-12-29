from django import forms
from django.contrib import admin
from blog.models import Article, Tag, Comment, Category,CategoryType

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('title','description','category','publish_time','update_time','hit_num',)
    list_filter = ('publish_time',)
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)

class CommentAdmin(admin.ModelAdmin):
    """docstring for CommentAdmin"""
    list_display = ('critic_name','article','email','content',)

class TagAdmin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('tag_name',)  

class CategoryAdmin(admin.ModelAdmin):
    """docstring for CategoryAdmin"""
    list_display = ('category_name',)

class CategoryTypeAdmin(admin.ModelAdmin):
    """docstring for CategoryAdmin"""
    list_display = ('categoryType_name',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryType, CategoryTypeAdmin)
