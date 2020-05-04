# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BookShelf, Book, BookPosition

# Register your models here.
@admin.register(BookShelf)
class BookShelf(admin.ModelAdmin):
    pass

@admin.register(BookPosition)
class BookPosition(admin.ModelAdmin):
    pass

@admin.register(Book)
class Book(admin.ModelAdmin):
    pass
