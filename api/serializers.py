from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import BookShelf, Book, BookPosition
from rest_auth.models import TokenModel
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class BookPositionSerializer(ModelSerializer):
    # bookShelf = SerializerMethodField()
    class Meta:
        model = BookPosition
        fields = [
            'id',
            'row_no',
            'column_no',
        ]

class BookSerializer(ModelSerializer):
    bookPosition = BookPositionSerializer()
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'cover',
            'isbn',
            'price',
            'publisher',
            'image',
            'created_at',
            'updated_at',
            'bookShelf',
            'bookPosition',
        ]


class UserSerializer(ModelSerializer):
    user_books = BookSerializer(many=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'user_books')

class BookShelfSerializer(ModelSerializer):
    books = BookSerializer(many=True, required=False)
    class Meta:
        model = BookShelf
        fields = [
            'id',
            'name',
            'description',
            'books'
        ]


class CustomTokenSerializer(ModelSerializer):
    class Meta:
        model = TokenModel
        fields = ('key', 'user')

