from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
     path('create-post/', views.createPost, name='create_post'),
    path('register/', views.register, name='register'),
]
