from django.urls import path
from . import views
urlpatterns = [
    path('',views.create),
    path('book_list',views.book_list),
]
#