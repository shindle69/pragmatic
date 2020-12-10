from django.contrib import admin


# Register your models here.
from articleapp.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','writer','content']

admin.site.register(Article, ArticleAdmin)