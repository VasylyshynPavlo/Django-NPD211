from django.urls import path
from LibraryApp import views

urlpatterns = [
    path('', views.collections, name='collections'),
    path('add/', views.add_collection, name='add_collection'),
    path('add-word/<int:collection_id>/', views.add_word, name='add_word'),
    path('edit-word/<int:word_id>/', views.edit_word, name='edit_word'),
    path('edit-collection/<int:collection_id>/', views.edit_collection, name='edit_collection'),
    path('delete-word/<int:word_id>/', views.delete_word, name='delete_word'),
    path('collections/<int:collection_id>/delete/', views.delete_collection, name='delete_collection'),
    path('world/', views.world_view, name='world'),
    path('collection/<int:collectionId>/', views.view_wordCollection_view, name='view_word_collection'),
    path('clone_collection/<int:collectionId>/', views.clone_wordCollection, name='clone_word_collection'),
]