from django.contrib import admin
from booktest.models import BookInfo, HeroInfo

# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "pub_date"]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["name", "gender", "comment", "book"]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
