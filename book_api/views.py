from django.shortcuts import render
from django.http import JsonResponse

from book_api.models import Book

from rest_framework.response import Response
from book_api.serializer import BookSerializer
from rest_framework.decorators import api_view

from rest_framework import status

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
    

@api_view(["GET"])
def book(request,id):
    try:
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    except:
        return Response({"error":"Eşleşen bir kayıt yok"}, status=status.HTT_NOT_FOUND)

@api_view(["POST"])
def book_update(request,id):
    book = Book.objects.get(pk=id)
    serializer =  BookSerializer(book,data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error)