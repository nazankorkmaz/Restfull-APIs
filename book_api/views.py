from django.shortcuts import render
from django.http import JsonResponse

from book_api.models import Book

from rest_framework.response import Response
from book_api.serializer import BookSerializer
from rest_framework.decorators import api_view

@api_view(["GET"])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many = True)
    return Response(serializer.data)
    """
    books_list = list(books.values())
    return JsonResponse({
        "books" : books_list
    })
    """

@api_view(["POST"])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)