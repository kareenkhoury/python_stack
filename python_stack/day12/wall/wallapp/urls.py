from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('registration', views.registration),
    path('login', views.login),  
    path('wall', views.wall), 
    path('clickpost/<id>', views.clickpost), 
    path('clickcomment', views.clickcomment), 
    path('delete/<int:id>', views.delete),
]