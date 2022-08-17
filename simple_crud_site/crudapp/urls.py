from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('create/', views.create, name='createview'),
    path('read/<int:id>', views.read, name='readview'),
    path('delete/', views.delete, name='deleteview'),
    path('update/<int:id>/', views.update, name='updateview'),
    path('createcmt/', views.create_comment),
]