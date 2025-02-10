from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>',views.book),
    path('',views.book_create),
    path('book_list/',views.book_list),
]
#