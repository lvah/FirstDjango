from django.contrib import admin
from .models import Book, Hero

# 后台管理的配置文件
# Register your models here.
admin.site.register(Book)
admin.site.register(Hero)
