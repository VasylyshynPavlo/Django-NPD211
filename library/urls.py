from library import views
from django.urls import path

urlpatterns = [  
    path('', views.home),
    path('details/<int:id>', views.user_detail),
]
