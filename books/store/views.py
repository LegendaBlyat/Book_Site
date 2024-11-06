
from rest_framework.viewsets import ModelViewSet

from store.models import Book
from store.serializers import BooksSerializers

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializers
