from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import BookShelf, Book


class BookSerializer(ModelSerializer):
    # bookShelf = SerializerMethodField()
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
        ]

    # def get_bookShelf(self, instance):
    #     return BookShelfSerialiser(BookShelf.objects.all()).data


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


