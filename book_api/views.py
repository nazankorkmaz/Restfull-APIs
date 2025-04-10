from django.shortcuts import render
from django.http import JsonResponse

from book_api.models import Book

from rest_framework.response import Response
from book_api.serializer import BookSerializer
from rest_framework.decorators import api_view

from rest_framework import status

#Bu tür işlemleri gerçekleştirebilmek için BookSerializer kullanılarak kitapların verisi doğrulanır, işlenir ve JSON formatında döndürülür.

@api_view(["GET"])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many = True)   # Birden fazla nesneyi serialize et #  tüm kitapları JSON formatına çevirir.
    return Response(serializer.data)  #JSON veriyi geri döndürür.
    """
    books_list = list(books.values())
    return JsonResponse({
        "books" : books_list
    })
    """

@api_view(["POST"])
def book_create(request):
    serializer = BookSerializer(data=request.data) #API'ye gelen JSON veriyi alır. veriyi deserialize etmek
    if serializer.is_valid(): # veri gecerli ise icerideki validasyonlari uygular
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

@api_view(["PUT"])
def book_update(request,id):
    book = Book.objects.get(pk=id) # Guncellenecek kitabi getir
    serializer =  BookSerializer(book,data = request.data)  #guncelle
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error)

@api_view(["DELETE"])
def book_delete(request,id):
    book = Book.objects.get(pk=id)
    book.delete()  #kitabi veritabanindan sil
    return Response(status= status.HTTP_204_NO_CONTENT)


"""
Tüm GET, POST, PUT, DELETE işlemlerinde Serializer şu şekilde çalışıyor:

Veritabanından gelen veri, serializer = BookSerializer(book) ile JSON formatına çevriliyor.
Kullanıcının gönderdiği JSON verisi, serializer = BookSerializer(data=request.data) ile deserialize ediliyor.
Validasyon kontrolü (is_valid()) yapılıyor.
Geçerliyse (serializer.save()) veri veritabanına kaydediliyor.

"""