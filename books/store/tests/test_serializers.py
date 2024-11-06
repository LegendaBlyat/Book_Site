from unittest import TestCase

from store.models import Book
from store.serializers import BooksSerializers


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Test Book 1', price=100.00, author='Jhon')
        book_2 = Book.objects.create(name='Test Book 2', price=150.00, author='Mario')
        data = BooksSerializers([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test Book 1',
                'price': '100.00',
                'author': 'Jhon',
            },
            {
                'id': book_2.id,
                'name': 'Test Book 2',
                'price': '150.00',
                'author': 'Mario',
            }
        ]
        self.assertEqual(expected_data, data)


