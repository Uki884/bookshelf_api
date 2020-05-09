# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BookShelf(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=120)

    def __str__(self):
        return self.name

class BookPosition(models.Model):
    column_no = models.IntegerField(verbose_name='本の列')
    row_no = models.IntegerField(verbose_name='本の行')

    def __str__(self):
        return str(self.id)

class Book(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=120)
    author = models.CharField(verbose_name='著者', max_length=120)
    cover = models.CharField(verbose_name='画像', max_length=500)
    isbn = models.CharField(verbose_name='ISBN', max_length=120)
    price = models.CharField(verbose_name='値段', blank=True, null=True, max_length=32)
    publisher = models.CharField(verbose_name='出版社', max_length=120)
    image = models.ImageField(verbose_name='アップロード画像', blank=True, null=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bookShelf = models.ForeignKey(BookShelf, verbose_name='本棚', related_name='books', blank=True, null=True, on_delete=models.CASCADE)
    bookPosition = models.OneToOneField(BookPosition, verbose_name='本の位置', blank=True, null=True, related_name='position', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='本登録者', related_name='user_books', blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

