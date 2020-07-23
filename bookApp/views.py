from django.shortcuts import render
from django.http import  HttpResponse
from .models import  Book

# Create your views here.
# 编写第一个视图函数, http协议(基于请求-响应的一个协议, request-response)
def index(request):
    return HttpResponse("图书管理系统")


def detail(request, id):
    """访问书籍详情信息的函数"""
    # 从Book书籍表中寻找id=1/2/3(url中需要查询的书籍id)的详细信息
    book = Book.objects.get(id=id)
    info = """
    书籍id: %s
    书籍名称: %s
    书籍发布日期:%s
    """ %(book.id, book.title, book.pub_date)
    # 视图函数,传入一个http请求,返回一个http响应
    return HttpResponse(info)




