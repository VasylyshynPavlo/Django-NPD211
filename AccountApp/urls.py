from django.contrib.auth import views as auth_views
from AccountApp import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('', views.home, name='home'),
]
