from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from booktest.models import BookInfo

# Create your views here.


# def my_render(request, template_path, context_dict={}):
#     # 加载html
#     template = loader.get_template(template_path)
#     # 拼接内容
#     # 渲染html
#     res_html = template.render(context_dict, request)
#     # 返回html
#     return HttpResponse(res_html)


def index(request):
    context = {"content": "我", "list": list(range(10))}
    # shortcuts
    # return my_render(request, "booktest/index.html", context)
    return render(request, "booktest/index.html", context)


def show_books(request):
    books = BookInfo.objects.all()
    context = {"books": books}
    return render(request, "booktest/show_books.html", context)


def detail(request, bid):
    book = BookInfo.objects.get(id=bid)
    heros = book.heroinfo_set.all()
    context = {"book": book, "heros": heros}
    return render(request, "booktest/detail.html", context)
