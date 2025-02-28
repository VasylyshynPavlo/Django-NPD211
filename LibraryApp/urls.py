from django.urls import path
from LibraryApp import views

urlpatterns = [
    path('', views.collections, name='collections'),
     path('add/', views.add_collection, name='add_collection'),
    path('add-word/<int:collection_id>/', views.add_word, name='add_word'),
    path('edit-word/<int:word_id>/', views.edit_word, name='edit_word'),
    path('delete-word/<int:word_id>/', views.delete_word, name='delete_word'),
]