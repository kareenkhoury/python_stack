from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('book/<int:book_id>/', views.bookview, name='bookview'),
    path('authors',views.addAuthors),
    path('authors/<int:number>',views.viewAuthor),
]