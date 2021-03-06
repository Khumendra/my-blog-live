from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<str:slug>/', views.blogpost, name='blogpost'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
]
