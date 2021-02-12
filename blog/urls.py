from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.blogHome, name="Blog Home"),
    path('<str:slug>', views.blogPost, name="Blog Post")
]
