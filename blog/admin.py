from blog.models import Article, Category, Comment
from django.contrib import admin

# Register your models here.

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)