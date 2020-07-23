from django.contrib import admin
from django.urls import path, re_path
# .代表当前目录， 从当前目录导入views模块
from . import  views

# 路由处理: 当客户端访问网址的时候， 交给哪一个函数去处理客户端的请求并返回响应。
urlpatterns = [
    # name='index'是给views.index起的一个别名，便于后续的处理
    path('', views.index, name='index'),
    # 设计访问书籍详情信息的url地址, 如下:
    # http://127.0.0.1:8000/book/1/
    # http://127.0.0.1:8000/book/2/
    # http://127.0.0.1:8000/book/3/
    # Django2中path的路由可以使用正则匹配, Django3中不能, 需要使用re_path
    # 正则的规则: [0-9]代表单个数字, \d也代表单个数字, +代表前面的字符出现1次或者多次.
    # 正则中的()代表分组,这里将()里面匹配到的内容传递给detail函数.
    # re_path('([0-9]+)/$', views.detail, name='detail'),
    # 注意: int代表整型, id代表将传入的整形数值存储到id变量中,传给视图函数
    path('<int:id>/', views.detail, name='detail')

]
