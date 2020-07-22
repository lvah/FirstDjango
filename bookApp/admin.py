from django.contrib import admin
from .models import Book, Hero

class HeroInline(admin.StackedInline):
    model = Hero
    extra = 2

# 书籍自定义管理页面
class BookAdmin(admin.ModelAdmin):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'title', 'pub_date']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['title', 'pub_date']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['title']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 3
    inlines =  [HeroInline]

# 人物自定义管理页面
class HeroAdmin(admin.ModelAdmin):
    # 后台管理查询需要的设置信息
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'name', 'sex', 'content', 'book']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['book']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['name']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 3

    # 后台管理添加需要设置的信息
    # fields = ['book', 'name', 'content', 'gender']
    fieldsets = [('基础信息', {'fields': ['book', 'name']}),
                 ('详细信息', {'fields': ['content', 'gender']}), ]




# 后台管理的配置文件
# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Hero, HeroAdmin)
