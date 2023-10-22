from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.registration),
    path('books', views.books),
    path('login', views.login),	
    path('createbook', views.createbook),
    path('books/<id>', views.viewbook),
    path('addfav/<book_id>/<user_id>', views.addfav),
    path('books', views.addfav),
    path('logout', views.logout),
    path('update/<book_id>', views.update),
    path('delete/<book_id>', views.delete),
    path('unfavorite/<book_id>', views.unfav)
]