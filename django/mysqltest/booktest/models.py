from django.db import models

# Create your models here.


class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateField()
    reads = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)


class HeroInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=False)
    comment = models.CharField(max_length=120)
    book = models.ForeignKey("BookInfo", on_delete=models.CASCADE, )
    isDelete = models.BooleanField(default=False)
