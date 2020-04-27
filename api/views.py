# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import BookShelf, Book, BookPosition
from .serializers import BookShelfSerializer, BookSerializer, BookPositionSerializer
import django_filters
from rest_framework import viewsets, filters
from rest_framework.response import Response

# Create your views here.


class BookShelfViewSet(viewsets.ModelViewSet):
    queryset = BookShelf.objects.all()
    serializer_class = BookShelfSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        # queryset = queryset.filter(bookShelf__isnull=True)
        return queryset

    def create(self, request):
        print(request.data)
        try:
            bookShelf = BookShelf.objects.get(id=request.data['bookShelf'])
            bookPosition = BookPosition.objects.create(column_no=request.data['column_no'], row_no=request.data['row_no'])
            book = Book.objects.create(
                title=request.data['title'],
                author=request.data['author'],
                cover=request.data['cover'],
                isbn=request.data['isbn'],
                price=request.POST.get('price', None),
                publisher=request.data['publisher'],
                image=request.POST.get('image', None),
                bookShelf=bookShelf,
                bookPosition=bookPosition
            )
            return Response(request.data, status=200)
        except Exception as e:
            print(e)
            return Response(request.data, status=500)

