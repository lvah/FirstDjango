from django.db import models


# Create your models here.
# 一个Book类对应一个数据库表
# 一个类属性对应一个数据库表的列属性
class Book(models.Model):
    # # 默认情况下，会自动添加id这一列作为主键。
    # title是字符串类型的， 并且最大的长度为20;
    title = models.CharField(max_length=20)
    pub_date = models.DateField()
    # 字符串的友好展示, 在交互式环境测试的时候生效
    def __repr__(self):
        return '<Book: %s>' % (self.title)
    # 字符串友好展示，在后台管理的时候生效
    def __str__(self):
        return self.title

    # 自定义对应的表名，默认表名：bookApp_book
    class Meta:
        db_table = "books"
        # 后台管理显示（单数）
        verbose_name = "图书管理"
        # 后台管理显示（复数）
        verbose_name_plural = "图书管理"


class Hero(models.Model):
    # 默认情况下，会自动添加id这一列作为主键。
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    content = models.CharField(max_length=200)
    # 一对多关系， 外键写在多的一端(Book:Hero=1:n)
    # models.CASCADE叫级联删除，当书籍被删除后，关联的任务也会被删除
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

    def __repr__(self):
        return "<Hero %s>" % (self.name)

    def __str__(self):
        return self.name

    # 自定义对应的表名，默认表名：bookApp_book
    class Meta:
        db_table = "heros"
        # 后台管理显示（单数）
        verbose_name = "人物管理"
        # 后台管理显示（复数）
        verbose_name_plural = "人物管理"
