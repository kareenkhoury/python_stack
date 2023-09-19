from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('destroy_session', views.reset),
 
]