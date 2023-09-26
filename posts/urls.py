from django.contrib import admin
from django.urls import path, include
from posts import views  # Import the views module from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', views.post_list, name='post_list'),
    path('posts/create/', views.create_post, name='create_post'),
]
