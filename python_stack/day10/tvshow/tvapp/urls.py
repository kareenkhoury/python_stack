from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('shows/new', views.addshow),
    path('shows/<id>', views.display),
    path('shows/<id>/edit', views.edit),
    path('submitshow/<id>', views.submitshow),
    path('shows/<id>/update', views.update),
    path('delete/<id>', views.delete),

]