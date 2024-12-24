from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create-post/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
