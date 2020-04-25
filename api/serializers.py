from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import BookShelf, Book, BookPosition


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
            'bookPosition'
        ]


class BookShelfSerializer(ModelSerializer):
    books = BookSerializer(many=True)
    class Meta:
        model = BookShelf
        fields = [
            'id',
            'name',
            'description',
            'books'
        ]



