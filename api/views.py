# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import BookShelf, Book
from .serializers import BookShelfSerializer, BookSerializer
import django_filters
from rest_framework import viewsets, filters

# Create your views here.


class BookShelfViewSet(viewsets.ModelViewSet):
    queryset = BookShelf.objects.all()
    serializer_class = BookShelfSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
