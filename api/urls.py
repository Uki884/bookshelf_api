# coding: utf-8

from rest_framework import routers
from .views import BookShelfViewSet, BookViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'book_shelf', BookShelfViewSet)
router.register(r'books', BookViewSet)
router.register(r'users', UserViewSet)
