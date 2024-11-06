from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Book
from store.serializers import BooksSerializers


class BooksApiTestCase(APITestCase):
    def test_get(self):
        book_1 = Book.objects.create(name='Test Book 1', price = 100.00, author='Jhon')
        book_2 = Book.objects.create(name='Test Book 2', price=150.00, author='Mario')
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BooksSerializers([book_1, book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

