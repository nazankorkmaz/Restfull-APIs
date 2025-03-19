from rest_framework import serializers
from book_api.models import Book

#model verisi json formatina cevirilir.
# Serializer, model verisini JSON formatına çevirir ve aynı zamanda doğrulama (validation) işlemleri yapar.
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length = 20)  # serilazerda otomatik validasyon yok bunu da eklemen lazim
    page_number = serializers.IntegerField()
    publish_data = serializers.DateField()
    stock = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)  #veritabanina kaydedilir
    
    # post istegi geldiginde direk burasi calisir
    """
    Bu method, yeni bir kitap kaydı oluşturmak için kullanılır.
    Nasıl Çalışır-> API'den validasyon kurallarına uygun bir JSON isteği gelir.
validated_data parametresi, doğrulanan verileri içerir.
Book.objects.create(**validated_data) ile yeni bir kitap kaydı veritabanına eklenir.
    """
    
    def update(self,instance, validated_data):
        instance.title = validated_data.get("title",instance.title)
        instance.page_number=validated_data.get("page_number",instance.page_number)
        instance.publish_data =validated_data.get("publish_data",instance.publish_data )
        instance.stock   = validated_data.get("stock",instance.stock )
        instance.save()
        return instance
    
    #  var olan bir kitabın bilgilerini güncellemek için kullanılır. Put metodu geldiginde calisir.
    """
    Güncellenecek kayıt (instance) alınır.
validated_data.get("title", instance.title) → Yeni bir title değeri gelirse günceller, gelmezse mevcut değeri korur.
instance.save() ile değişiklikler veritabanına kaydedilir.
Güncellenmiş nesne geri döndürülür.
    """