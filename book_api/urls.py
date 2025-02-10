from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>',views.book),
    path('',views.book_create),
    path('update/<int:id>',views.book_update),
    path('delete/<int:id>',views.book_delete),
    path('book_list/',views.book_list),
]
#