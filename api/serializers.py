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
            'cover',  # モデルには存在しない追加する新フィールド
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
class BookShelfSerialiser(ModelSerializer):
    books = SerializerMethodField()
    class Meta:
        model = BookShelf
        fields = [
            'id',
            'name',
            'description',
            'books',  # モデルには存在しない追加する新フィールド
        ]

    def get_books(self, instance):
        return BookSerializer(Book.objects.get()).data


