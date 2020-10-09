from django.shortcuts import render, redirect
from booktest.models import BookInfo
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def index(request):
    books = BookInfo.objects.all()
    context = {"books": books}
    return render(request, "booktest/index.html", context)


def create(request):
    b = BookInfo()
    b.title = "流星蝴蝶剑"
    b.pub_date = date(1990, 1, 1)
    b.save()
    # return HttpResponseRedirect("/index")
    return redirect("/index")


def delete(request, bid):
    book = BookInfo.objects.get(id=bid)
    book.delete()
    # return HttpResponseRedirect("/index")
    return redirect("/index")
